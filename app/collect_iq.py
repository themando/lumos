#!/usr/bin/env python


"""
Read samples from a UHD device and write to file formatted as binary
outputs single precision complex float values or complex short values 
(interleaved 16 bit signed short integers).
"""

from gnuradio import gr, gru, eng_notation
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from optparse import OptionParser
import sys

n2s = eng_notation.num_to_str

class rx_cfile_block(gr.top_block):

    def __init__(self, options, filename):
        gr.top_block.__init__(self)

        scalar="scalar="+str(options.scalar)
        # Create a UHD device source
        if options.output_shorts:
            self._u = uhd.usrp_source(device_addr=options.args, stream_args=uhd.stream_args('sc16',
                                      options.wire_format, args=scalar))
            self._sink = gr.file_sink(gr.sizeof_short*2, filename)
        else:
            self._u = uhd.usrp_source(device_addr=options.args, stream_args=uhd.stream_args('fc32',
                                      options.wire_format, args=scalar))
            self._sink = gr.file_sink(gr.sizeof_gr_complex, filename)

        # Set the subdevice spec
        if(options.spec):
            self._u.set_subdev_spec(options.spec, 0)

        # Set the antenna
        if(options.antenna):
            self._u.set_antenna(options.antenna, 0)

        # Set receiver sample rate
        self._u.set_samp_rate(options.samp_rate)

        # Set receive daughterboard gain
        if options.gain is None:
            g = self._u.get_gain_range()
            options.gain = float(g.start()+g.stop())/2
	    print "Using mid-point gain of", options.gain, "(", g.start(), "-", g.stop(), ")"
        self._u.set_gain(options.gain)

        # Set frequency (tune request takes lo_offset)
        if(options.lo_offset is not None):
            treq = uhd.tune_request(options.freq, options.lo_offset)
        else:
            treq = uhd.tune_request(options.freq)
        tr = self._u.set_center_freq(treq)
        if tr == None:
            sys.stderr.write('Failed to set center frequency\n')
            raise SystemExit, 1

        # Create head block if needed and wire it up
        if options.nsamples is None:
            self.connect(self._u, self._sink)
        else:
            if options.output_shorts:
                self._head = gr.head(gr.sizeof_short*2, int(options.nsamples))
            else:
                self._head = gr.head(gr.sizeof_gr_complex, int(options.nsamples))

            self.connect(self._u, self._head, self._sink)

        input_rate = self._u.get_samp_rate()
        
        if options.verbose:
            print "Args: ", options.args
            print "Rx gain:", options.gain
            print "Rx baseband frequency:", n2s(tr.actual_rf_freq)
            print "Rx DDC frequency:", n2s(tr.actual_dsp_freq)
            print "Rx Sample Rate:", n2s(input_rate)
            if options.nsamples is None:
                print "Receiving samples until Ctrl-C"
            else:
                print "Receving", n2s(options.nsamples), "samples"
            if options.output_shorts:
                print "Writing 16-bit complex shorts"
            else:
                print "Writing 32-bit complex floats"
            print "Output filename:", filename

        # Direct asynchronous notifications to callback function
        if options.show_async_msg:
            self.async_msgq = gr.msg_queue(0)
            self.async_src = uhd.amsg_source("", self.async_msgq)
            self.async_rcv = gru.msgq_runner(self.async_msgq, self.async_callback)

    def async_callback(self, msg):
        md = self.async_src.msg_to_async_metadata_t(msg)
        print "Channel: %i Time: %f Event: %i" % (md.channel, md.time_spec.get_real_secs(), md.event_code)

        
def get_options():
    usage="%prog: [options] output_filename"
    parser = OptionParser(option_class=eng_option, usage=usage)
    parser.add_option("-a", "--args", type="string", default="",
                      help="UHD device address args , [default=%default]")
    parser.add_option("", "--spec", type="string", default=None,
                      help="Subdevice of UHD device where appropriate")
    parser.add_option("-A", "--antenna", type="string", default=None,
                      help="select Rx Antenna where appropriate")
    parser.add_option("", "--samp-rate", type="eng_float", default=1e6,
                      help="set sample rate (bandwidth) [default=%default]")
    parser.add_option("-f", "--freq", type="eng_float", default=None,
                      help="set frequency to FREQ", metavar="FREQ")
    parser.add_option("-g", "--gain", type="eng_float", default=None,
                      help="set gain in dB (default is midpoint)")
    parser.add_option( "-s","--output-shorts", action="store_true", default=False,
                      help="output interleaved shorts instead of complex floats")
    parser.add_option("-N", "--nsamples", type="eng_float", default=None,
                      help="number of samples to collect [default=+inf]")
    parser.add_option("-v", "--verbose", action="store_true", default=False,
                      help="verbose output")
    parser.add_option("", "--lo-offset", type="eng_float", default=None,
                      help="set daughterboard LO offset to OFFSET [default=hw default]")
    parser.add_option("", "--wire-format", type="string", default="sc16",
                      help="set wire format from USRP [default=%default")
    parser.add_option("", "--scalar", type="int", default=1024,
                      help="set scalar multiplier value for sc8 wire format [default=%default]")
    parser.add_option("", "--show-async-msg", action="store_true", default=False,
                      help="Show asynchronous message notifications from UHD [default=%default]")

    (options, args) = parser.parse_args ()
    if len(args) != 1:
        parser.print_help()
        raise SystemExit, 1
    
    if options.freq is None:
        parser.print_help()
        sys.stderr.write('You must specify the frequency with -f FREQ\n');
        raise SystemExit, 1
    
    return (options, args[0])


if __name__ == '__main__':
    (options, filename) = get_options()
    tb = rx_cfile_block(options, filename)
    
    try:
        tb.run()
    except KeyboardInterrupt:
        pass