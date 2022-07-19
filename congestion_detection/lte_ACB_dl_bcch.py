
#import packages

import json
import os
import glob
from collections import defaultdict
import csv



# Declare the base directories for json files and the future csv files

# base_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/dl_bcch/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/uncongested/analysis/"


# base_dir = "../data/drone_LTE/LTE_data_graduation/final_graduation/json_dl_bcch/bren/"
# sec_dir = "../data/drone_LTE/LTE_data_graduation/final_graduation/analysis/"


base_dir = "../data/backup/LTE_congestion/SanDiego/dl_bcch/botanical_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/botanical_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

BarringFactor = []
BarringTime = []

BarringForSpecialAC = []
nonCritical_opt1 = []

sample_test = []
count = []

# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory


		json_data = json.load(in_file)

		

		for i in xrange(0, len(json_data)):


			# Since not all of the frames have BarringInfo key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory
			try:
				for items in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"]:
					# print items

					if "lte-rrc.ac_BarringForMO_Data_element" or "lte-rrc.ac_BarringForMO_Signalling_element" in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]:


						epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
						frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])


						if "lte-rrc.ac_BarringForMO_Data_element" not in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]:

							BarringFactor.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Signalling_element"]["lte-rrc.ac_BarringFactor"])
						
							BarringTime.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Signalling_element"]["lte-rrc.ac_BarringTime"])

							BarringForSpecialAC.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Signalling_element"]["lte-rrc.ac_BarringTime"])

						else:

							BarringFactor.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Data_element"]["lte-rrc.ac_BarringFactor"])
							
							BarringTime.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Data_element"]["lte-rrc.ac_BarringTime"])

							BarringForSpecialAC.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Data_element"]["lte-rrc.ac_BarringTime"])

						nonCritical_opt1.append("NA")

						count.append(1)

						sample_test.append(1)

			except Exception, e:
				# print e
				pass
		
		
		
print len(sample_test)
# print epoch, frame_no, reject_opt_field, wait_time, lateNonCriticalExtention_len, nonCritical_opt1

os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, BarringFactor, BarringTime, BarringForSpecialAC, nonCritical_opt1, count)

with open('uncongested_botanical_night_ACB.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "Barring Factor", "Barring Time", "BarringForSpecialAC", "nonCritical Field", "count"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()










base_dir = "../data/backup/LTE_congestion/SanDiego/dl_bcch/horton_night/"
sec_dir = "../data/backup/LTE_congestion/SanDiego/analysis/horton_night/"

os.chdir(base_dir)

# Declare the lists for all the parameters we want to extract
epoch = []
frame_no = []

BarringFactor = []
BarringTime = []

BarringForSpecialAC = []
nonCritical_opt1 = []

sample_test = []
count = []

# Query all the files in the said folder

for files in (glob.glob('*')):
	print files

	with open(files, 'r') as in_file:
		# load the json data onto memory


		json_data = json.load(in_file)

		

		for i in xrange(0, len(json_data)):


			# Since not all of the frames have BarringInfo key, try to find the ones which do. Extracting all the values that we're interested in. Nomenclature is self-explanatory
			try:
				for items in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"]:
					# print items

					if "lte-rrc.ac_BarringForMO_Data_element" or "lte-rrc.ac_BarringForMO_Signalling_element" in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]:


						epoch.append(json_data[i]["_source"]["layers"]["frame"]["frame.time_epoch"])
						frame_no.append(json_data[i]["_source"]["layers"]["frame"]["frame.number"])


						if "lte-rrc.ac_BarringForMO_Data_element" not in json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]:

							BarringFactor.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Signalling_element"]["lte-rrc.ac_BarringFactor"])
						
							BarringTime.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Signalling_element"]["lte-rrc.ac_BarringTime"])

							BarringForSpecialAC.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Signalling_element"]["lte-rrc.ac_BarringTime"])

						else:

							BarringFactor.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Data_element"]["lte-rrc.ac_BarringFactor"])
							
							BarringTime.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Data_element"]["lte-rrc.ac_BarringTime"])

							BarringForSpecialAC.append(json_data[i]["_source"]["layers"]["lte-rrc.BCCH_DL_SCH_Message_element"]["lte-rrc.message_tree"]["lte-rrc.c1_tree"]["lte-rrc.systemInformation_element"]["lte-rrc.criticalExtensions_tree"]["lte-rrc.systemInformation_r8_element"]["lte-rrc.sib_TypeAndInfo_tree"][items]["lte-rrc.sib_TypeAndInfo_item_tree"]["lte-rrc.sib2_element"]["lte-rrc.ac_BarringInfo_element"]["lte-rrc.ac_BarringForMO_Data_element"]["lte-rrc.ac_BarringTime"])

						nonCritical_opt1.append("NA")

						count.append(1)

						sample_test.append(1)

			except Exception, e:
				# print e
				pass
		
		
		
print len(sample_test)
# print epoch, frame_no, reject_opt_field, wait_time, lateNonCriticalExtention_len, nonCritical_opt1

os.chdir(sec_dir)

# Writing all into a csv file. We will be writing all the lists as the columns of the csv.

export_data = zip(frame_no, epoch, BarringFactor, BarringTime, BarringForSpecialAC, nonCritical_opt1, count)

with open('uncongested_horton_night_ACB.csv', 'w') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Frame Number", "Epoch", "Barring Factor", "Barring Time", "BarringForSpecialAC", "nonCritical Field", "count"))
      for rows in export_data:
      	wr.writerow(rows)
myfile.close()
