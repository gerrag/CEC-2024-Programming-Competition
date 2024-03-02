###############################################################################
#
#   File : interpreter.py
#   Summary: This script reads in data sets wtih respect to user input of what is requested
#   Project: CEC 2024
#   Authors: Gary, Daigh, Abraham, Connor
#
###############################################################################

import numpy as np
import csv

#GLOBAL VARIABLES
MAX_VALUE = float('-inf')
MIN_VALUE = float('inf')

#FUNCTION - singleInterpreter
#Input - single day file (helium, metal, etc.)
#Output - 2d array of MAP (cols: x,rows: y) with values
#NOTES: Only interprets cols(?, x, y, value) from a dataset 
def singleInterpreter(data_file_name, day):
    
    data_file_name = f"data/{data_file_name}_data_day_{day}.csv"

    with open(data_file_name) as data:
        
        #Interpreting CSV -> 2D np.array
        data_list = list(csv.reader(data, delimiter=","))
        data_list = np.array(data_list)

        #Removing headers, and first garbage column
        data_list = np.delete(data_list, 0, 1)
        data_list = np.delete(data_list, 0, 0)

        #Map Creation
        map = np.zeros(shape=(100,100))
        for row in data_list:
            x_value = int(row[0])
            y_value = int(row[1])

            value = row[2]
            if value == '':
                value = 0
            else:
                value = float(value)

            map[y_value][x_value] = value

        #Removing Invalid Choices (Land vs Water)
        #TO BE CONTINUED
    

#FUNCTION - multiInterpreter
#Input - 
#Output - 
#NOTES: 

#FUNCTION - normalizationValueReplacement
#Input -  
#Output - 
#NOTES: 

#main
#Input - 
def main(input):

    return 

singleInterpreter("algal", 1)