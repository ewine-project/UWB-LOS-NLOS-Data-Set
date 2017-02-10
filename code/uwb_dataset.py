"""
Created on Feb 6, 2017

@author: Klemen Bregar 
"""

import os
import pandas as pd
from numpy import vstack


def import_from_files():
    """
        Read .csv files and store data into an array
        format: |LOS|NLOS|data...|
    """
    rootdir = '../dataset/'
    output_arr = []
    first = 1
    for dirpath, dirnames, filenames in os.walk(rootdir):
        for file in filenames:
            filename = os.path.join(dirpath, file)
            print(filename)
            output_data = [] 
            # read data from file
            df = pd.read_csv(filename, sep=',', header=0)
            input_data = df.as_matrix()
            # append to array
            if first > 0:
                first = 0
                output_arr = input_data
            else:
                output_arr = vstack((output_arr, input_data))
    
    return output_arr

if __name__ == '__main__':

    # import raw data from folder with dataset
    print("Importing dataset to numpy array")
    print("-------------------------------")
    data = import_from_files()
    print("-------------------------------")
    # print dimensions and data
    print("Number of samples in dataset: %d" % len(data))
    print("Length of one sample: %d" % len(data[0]))
    print("-------------------------------")
    print("Dataset:")
    print(data)