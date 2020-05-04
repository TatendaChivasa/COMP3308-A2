import sys
import numpy as np
import os
import csv

def main():

    argc = len(sys.argv)
    if argc < 3:
        print("Program did not receive the number of parameters needed to run")
        sys.exit()

    training = sys.argv[1]
    testing = sys.argv[2]
    algorithm = sys.argv[3]

    if "NN" in algorithm:
        k = algorithm[0]
        kNN(k, training, testing)
  
    #WHAT IF DATA IS MISSING

def kNN(k, training, testing): #open files see if i need to extract the first column out 
    testing_file = open(testing, "r" )
    training_file = open(training, "r")
    # print("in knn")

    training_array = []
    if os.path.exists(training):
        with open(training) as File2:
            for row in csv.reader(File2, delimiter= ',', skipinitialspace= True):
                training_array.append(row) #the length of each entry tells us how many columns there are 
#     training_array.pop(0) #remove the title column


    testing_array = []
    if os.path.exists(testing):
        with open(testing) as File:
            for row in csv.reader(File, delimiter= ',', skipinitialspace= True):
                testing_array.append(row) #the length of each entry tells us how many columns there are 
#     testing_array.pop(0) #remove the title column
    lengthh = len(testing_array[0]) #shows you where to access the 
    class_t = testing_array[0][(lengthh-1)] #how to access the class
    # print("class", class_t)
    # print(type(class_t))
    # print(type(testing_array[0][0]))
    
    # print("testing", testing_array)

    # print("\ntraining", testing_array)

    #classification compare with new value with ever training example






if __name__ == "__main__":
    main()
