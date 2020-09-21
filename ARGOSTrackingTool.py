#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Annika Socha (as986@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#create a variable pointing to the data file
file_name = "./data/raw/Sara.txt"

#create a file object from the file
file_object = open(file_name, "r")

#read the entire contents of file into a list
line_list = file_object.readlines()

#close the file
file_object.close()

#pretend we read one line of data from the file
for lineString in line_list:
    if lineString[0] in ("#", "u"): continue  #skip lines that start with # and u
    #split the string into list of data items
    lineData = lineString.split()
    #assign variable to specific items in list
    record_id = lineData[0]    #ARGOS tracking record ID
    obs_date = lineData[2]    #Observation date
    obs_lc = lineData[4]    #observation location class
    obs_lat = lineData[6]   #obs latitude
    obs_lon = lineData[7]   #obs longitude

#print location of sara
print(f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
