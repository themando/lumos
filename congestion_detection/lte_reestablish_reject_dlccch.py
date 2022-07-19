
#import packages

import json
import os
import glob
from collections import defaultdict
# import pandas as pd
import csv
# from itertools import cdzip


# Declare the base directories for json files and the future csv files

# base_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/dl_ccch/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/analysis/"


# base_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/sample/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/sample/"



base_dir = "../data/backup/LTE_congestion/SanDiego/dl_ccch/botanical_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/botanical_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

reject_opt_field = []
wait_time = []

lateNonCriticalExtention_len = []
nonCritical_opt1 = []
nonCritical_opt2 = []
total_pkts = []
count = []
# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory

		json_data = json.load(in_file)

		total_pkts.append(len(json_data))

		for i in xrange(0, len(json_data)):
			
			# Since not all of the frames have ConnectionReject key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory
			# print(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"])
			try:
				if "lte-rrc.rrcConnectionReestablishmentReject_r8_element" in json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]:
					

					epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
					frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])

					reject_opt_field.append(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentReject_r8_element"]["per.optional_field_bit"])

				
					wait_time.append("NA")

					try:

						lateNonCriticalExtention_len.append(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentReject_r8_element"]["lte-rrc.nonCriticalExtension_element"]["per.octet_string_length"])
						nonCritical_opt1.append(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentReject_r8_element"]["lte-rrc.nonCriticalExtension_element"]["per.optional_field_bit"])
						


					except KeyError, e:	

						lateNonCriticalExtention_len.append("NA")

						nonCritical_opt1.append("NA")
						
					count.append(1)


			except KeyError, e:
				#ignore key erros for redundant frames 
				pass
				# print 'I got a KeyError - reason "%s"' % str(e)

	# print epoch, frame_no, reject_opt_field, wait_time, lateNonCriticalExtention_len, nonCritical_opt1

os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, reject_opt_field, wait_time, lateNonCriticalExtention_len, nonCritical_opt1, count)
# print export_data
# export_data = zip_longest(*d, fillvalue = '')
with open('uncongested_botanical_night_reestablish_reject.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "Reject OptField", "Wait Time", "Payload Length", "nonCritical Field", "count"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()

print(sum(total_pkts))









base_dir = "../data/backup/LTE_congestion/SanDiego/dl_ccch/horton_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/horton_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

reject_opt_field = []
wait_time = []

lateNonCriticalExtention_len = []
nonCritical_opt1 = []
nonCritical_opt2 = []
total_pkts = []
count = []
# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory

		json_data = json.load(in_file)

		total_pkts.append(len(json_data))

		for i in xrange(0, len(json_data)):
			
			# Since not all of the frames have ConnectionReject key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory
			# print(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"])
			try:
				if "lte-rrc.rrcConnectionReestablishmentReject_r8_element" in json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]:
					

					epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
					frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])

					reject_opt_field.append(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentReject_r8_element"]["per.optional_field_bit"])

				
					wait_time.append("NA")

					try:

						lateNonCriticalExtention_len.append(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentReject_r8_element"]["lte-rrc.nonCriticalExtension_element"]["per.octet_string_length"])
						nonCritical_opt1.append(json_data[i]["_source"]["layers"]["lte-rrc.DL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentReject_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentReject_r8_element"]["lte-rrc.nonCriticalExtension_element"]["per.optional_field_bit"])
						


					except KeyError, e:	

						lateNonCriticalExtention_len.append("NA")

						nonCritical_opt1.append("NA")
						
					count.append(1)


			except KeyError, e:
				#ignore key erros for redundant frames 
				pass
				# print 'I got a KeyError - reason "%s"' % str(e)

	# print epoch, frame_no, reject_opt_field, wait_time, lateNonCriticalExtention_len, nonCritical_opt1

os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, reject_opt_field, wait_time, lateNonCriticalExtention_len, nonCritical_opt1, count)
# print export_data
# export_data = zip_longest(*d, fillvalue = '')
with open('uncongested_horton_night_reestablish_reject.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "Reject OptField", "Wait Time", "Payload Length", "nonCritical Field", "count"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()

print(sum(total_pkts))