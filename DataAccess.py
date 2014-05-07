import csv 
import numpy
import os 

class ReadFromCSV:
    
#     _header = None    # holds the data headers
#     _csvdata = []     # holds the csv data
#     _rawdata = None   # holds the raw data from csv (excluding header)

    # header property
    def Header(self):
        return self.__header
    
    # rawdata as numpy list property
    def RawDataAsNumpy(self):
        return self.__RawDataAsNumpy.T
    
    # csvdata property
    def CsvData(self):
        return self.__CsvData
    
    # constructor
    def __init__(self, folder, filename, hasheader, dirname = os.path.dirname(__file__)):
        
        # open csv file and load into a python object ( the dir of this file is used if no dirname is input)
        try:
            # pc path pattern
            self.__csvObj = csv.reader(open(dirname + "\\" + folder + "\\" + filename, 'rb'), quoting = csv.QUOTE_NONNUMERIC)
        except:
            # mac path pattern
            self.__csvObj = csv.reader(open(dirname + "/" + folder + "/" + filename, 'rb'), quoting = csv.QUOTE_NONNUMERIC)
        
        # if csv file has a header then store the header and skip the first line
        if(hasheader): self.__header = numpy.array(self.__csvObj.next())
            
        # loop through rows in csv file and get data
        self.__CsvData = []
        for row in self.__csvObj:
            self.__CsvData.append(row)
        
        # convert to numpy array
        self.__RawDataAsNumpy = numpy.array(self.__CsvData)


      
class WriteToCSV:
    
    def csvObj(self):
        return self.__csvObj
        
    def __init__(self, folder, filename, hasheader, dirname = os.path.dirname(__file__)):
        
        try:
            # pc path pattern
            self.__csvObj = csv.writer(open(dirname + "\\" + folder + "\\" + filename, 'wb'))
        except:
            # mac path pattern
            self.__csvObj = csv.writer(open(dirname + "/" + folder + "/" + filename, 'wb'))