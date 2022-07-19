
#import packages

import json
import os
import glob
from collections import defaultdict

import csv



# Declare the base directories for json files and the future csv files

# base_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/ul_ccch/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/analysis/"


# base_dir = "../data/drone_LTE/LTE_data_graduation/final_graduation/json_ul_ccch/graduation/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/final_graduation/analysis/"



base_dir = "../data/backup/LTE_congestion/SanDiego/ul_ccch/botanical_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/botanical_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

RNTI = []
physCellId = []
shortMAC =[]
establishCause =[]
count = []
total_pkts = []
# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory

		json_data = json.load(in_file)

		total_pkts.append(len(json_data))

		for i in xrange(0, len(json_data)):


			
			# Since not all of the frames have ConnectionReject key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory

			try:
				
				# Checking for those frames which containe Requests

				if "lte-rrc.rrcConnectionReestablishmentRequest_r8_element" in json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]:
					
					
					epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
					frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])

					RNTI.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.ue_Identity_element"]["lte-rrc.c_RNTI"])

					physCellId.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.ue_Identity_element"]["lte-rrc.physCellId"])

					shortMAC.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.ue_Identity_element"]["lte-rrc.shortMAC_I"])



					establishCause.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.reestablishmentCause"])

						
					count.append(1)


			except KeyError, e:
				#ignore key erros for redundant frames 
				pass


print epoch, frame_no, RNTI, physCellId, shortMAC, establishCause

os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, RNTI, physCellId, shortMAC, establishCause, count)

with open('uncongested_botanical_night_reestablish_request.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "RNTI", "physCellId", "shortMAC", "establishCause", "Count"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()








base_dir = "../data/backup/LTE_congestion/SanDiego/ul_ccch/horton_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/horton_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

RNTI = []
physCellId = []
shortMAC =[]
establishCause =[]
count = []
total_pkts = []
# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory

		json_data = json.load(in_file)

		total_pkts.append(len(json_data))

		for i in xrange(0, len(json_data)):


			
			# Since not all of the frames have ConnectionReject key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory

			try:
				
				# Checking for those frames which containe Requests

				if "lte-rrc.rrcConnectionReestablishmentRequest_r8_element" in json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]:
					
					
					epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
					frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])

					RNTI.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.ue_Identity_element"]["lte-rrc.c_RNTI"])

					physCellId.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.ue_Identity_element"]["lte-rrc.physCellId"])

					shortMAC.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.ue_Identity_element"]["lte-rrc.shortMAC_I"])



					establishCause.append(json_data[i]["_source"]["layers"]["lte-rrc.UL_CCCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.rrcConnectionReestablishmentRequest_r8_element"]["lte-rrc.reestablishmentCause"])

						
					count.append(1)


			except KeyError, e:
				#ignore key erros for redundant frames 
				pass


print epoch, frame_no, RNTI, physCellId, shortMAC, establishCause

os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, RNTI, physCellId, shortMAC, establishCause, count)

with open('uncongested_horton_night_reestablish_request.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "RNTI", "physCellId", "shortMAC", "establishCause", "Count"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()