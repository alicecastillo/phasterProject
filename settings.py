# contains list of all assumptions necessary for program execution

#init all globals

def init(urlString): 
    global url, jsonFile, runNum, runTimes, badAccessions
    url = urlString
    jsonFile = "phaster_io_output.txt"
    runNum = 33 #CHANGE THIS BACK
    runTimes = 0
    badAccessions = []
    pausedAccessions = []