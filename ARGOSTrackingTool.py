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

#pretend we read one line of data from the file
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

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
