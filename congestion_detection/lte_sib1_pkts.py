
#import packages

import json
import os
import glob
from collections import defaultdict
import csv



# Declare the base directories for json files and the future csv files

# base_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/dl_bcch/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/analysis/"


# base_dir = "../data/drone_LTE/LTE_data_graduation/final_graduation/json_dl_bcch/graduation/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/final_graduation/analysis/"



base_dir = "../data/backup/LTE_congestion/SanDiego/dl_bcch/botanical_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/botanical_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

cellReservedForOperatorUse = []
cellBarred = []
RxLevMin = []

FreqBandIndicator = []
sib1 = []

# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory

		json_data = json.load(in_file)



		for i in xrange(0, len(json_data)):


			
			# Since not all of the frames have ConnectionReject key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory

			try:
				
				# Checking for those frames which containe Requests

				if "lte-rrc.systemInformationBlockType1_element" in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]:

					epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
					frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])
					
					cellReservedForOperatorUse.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.cellAccessRelatedInfo_element"]["lte-rrc.plmn_IdentityList_tree"]["Item 0"]["lte-rrc.PLMN_IdentityInfo_element"]["lte-rrc.cellReservedForOperatorUse"])

					cellBarred.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.cellAccessRelatedInfo_element"]["lte-rrc.cellBarred"])

					RxLevMin.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.cellSelectionInfo_element"]["lte-rrc.q_RxLevMin"])

					FreqBandIndicator.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.freqBandIndicator"])

					sib1.append(1)

			except KeyError, e:
				#ignore key erros for redundant frames 
				pass




os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, cellReservedForOperatorUse, cellBarred, RxLevMin, FreqBandIndicator, sib1)

with open('uncongested_botanical_night_sib1.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "cellReservedForOperatorUse", "cellBarred", "RxLevMin", "FreqBandIndicator", "sib1"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()







base_dir = "../data/backup/LTE_congestion/SanDiego/dl_bcch/horton_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/horton_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

cellReservedForOperatorUse = []
cellBarred = []
RxLevMin = []

FreqBandIndicator = []
sib1 = []

# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory

		json_data = json.load(in_file)



		for i in xrange(0, len(json_data)):


			
			# Since not all of the frames have ConnectionReject key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory

			try:
				
				# Checking for those frames which containe Requests

				if "lte-rrc.systemInformationBlockType1_element" in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]:

					epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
					frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])
					
					cellReservedForOperatorUse.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.cellAccessRelatedInfo_element"]["lte-rrc.plmn_IdentityList_tree"]["Item 0"]["lte-rrc.PLMN_IdentityInfo_element"]["lte-rrc.cellReservedForOperatorUse"])

					cellBarred.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.cellAccessRelatedInfo_element"]["lte-rrc.cellBarred"])

					RxLevMin.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.cellSelectionInfo_element"]["lte-rrc.q_RxLevMin"])

					FreqBandIndicator.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformationBlockType1_element"]["lte-rrc.freqBandIndicator"])

					sib1.append(1)

			except KeyError, e:
				#ignore key erros for redundant frames 
				pass




os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, cellReservedForOperatorUse, cellBarred, RxLevMin, FreqBandIndicator, sib1)

with open('uncongested_horton_night_sib1.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "cellReservedForOperatorUse", "cellBarred", "RxLevMin", "FreqBandIndicator", "sib1"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()