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
import os
from matplotlib import pyplot as plt

#GLOBAL VARIABLES
MAX_VALUE = float('-inf')
MIN_VALUE = float('inf')

#------------ HELPER FUNCTIONS ------------
#FUNCTION - worldArray
#Output - 2x100 Array of 0s and 1s classifying land and water
#NOTES: ASSUMPTION THAT world_array_data_set_day_1 DOES NOT CHANGE W.R.T DAYS BEYOND!!!
def worldArray():
    file_dir = os.path.dirname(__file__)
    file_name = os.path.join(file_dir, '../data/world_array_data_day_1.csv')
    with open(file_name) as data:
        data_list = dataListCreation(data)

    return data_list

#FUNCTION - dataListCreation
#Output - 2x100 Array of 0s and 1s classifying land and water sorted
#NOTES: ASSUMPTION THAT follows this format of cols: (?,x,y,value)
def dataListCreation(data):

    #Interpreting CSV -> 2D np.array
    data_list = list(csv.reader(data, delimiter=","))
    data_list = np.array(data_list)

    #Removing headers, and first garbage column
    data_list = np.delete(data_list, 0, 1)
    data_list = np.delete(data_list, 0, 0)

    return data_list

#------------ HELPER FUNCTIONS ------------
#FUNCTION - singleInterpreter
#Input - single day file (helium, metal, etc.)
#Output - 2d array of MAP (cols: x,rows: y) with values
#NOTES: Only interprets cols(?, x, y, value) from a dataset 
def singleInterpreter(data_file_name, day):
    global MAX_VALUE
    global MIN_VALUE
    file_dir = os.path.dirname(__file__)
    file_name = os.path.join(file_dir, f'../data/{data_file_name}_data_day_{day}.csv')
   
   #Data List Creation of interpreted file
    with open(file_name) as data:
        data_list = dataListCreation(data)


    #Map Creation & Removal of Invalid Values (Land vs Water)
    world = worldArray()
    map = np.zeros(shape=(100,100))
    for row in data_list:
        #Map Creation
        x_value = int(row[0])
        y_value = int(row[1])

        value = row[2]
        if value == '':
            value = 0
        else:
            value = float(value)

        map[y_value][x_value] = value

    #Removal of Invalid Values & Keep Track of MAX_VAL AND MIN_VAL
    for row in world:
        x_value = int(row[0])
        y_value = int(row[1])
        land_water = int(row[2])

        if (land_water == 1):
            map[y_value][x_value] = -1
        else: 
            if (map[y_value][x_value] > MAX_VALUE):
                MAX_VALUE = map[y_value][x_value]
            elif (map[y_value][x_value] < MIN_VALUE):
                MIN_VALUE = map[y_value][x_value]

    return map

#FUNCTION - multiInterpreter
#Input - input from main for which data is required for mapping
#Output - 3D array of maps as (1 dimension (width) as total days, 2 dimensions of x,y map of values)


#main
#Input - 
def main(input):

    return

singleInterpreter("algal", 30)