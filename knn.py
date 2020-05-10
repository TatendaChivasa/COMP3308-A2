import sys
import numpy as np
import os
import csv
import math 
from statistics import mode

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
    output_classes = []

    training_array = []
    if os.path.exists(training):
        with open(training) as File2:
            for row in csv.reader(File2, delimiter= ','):
                training_array.append(row) #the length of each entry tells us how many columns there are 
    # training_array.pop(0) #remove the title column


    testing_array = []
    if os.path.exists(testing):
        with open(testing) as File:
            for row in csv.reader(File, delimiter= ','):
                testing_array.append(row) #the length of each entry tells us how many columns there are 
    # testing_array.pop(0) #remove the title column
    lengthh = len(testing_array[0]) #shows you where to access the 
    class_t = testing_array[0][(lengthh-1)] #how to access the class
    # print("class", class_t)
    # print(type(class_t))
    # print(type(testing_array[0][0]))

    #classification compare with new value with ever training example
    #calculate the euclidean distance
    for test in testing_array: #one row in the testing dataset
        for train in training_array: #go through all the rows in the training dataset
            length = len(test) # train = n+ 1 with class column and test = n should have the same length
            distance = 0.0
            e_distance = [] 
            for n in range(0, length-1): # going through all the elements to get the euclidean distance
                #print(train)
                #print(test)
                d = (float(train[n]) - float(test[n])) ** 2 #square the differnce 
                distance = distance + d
            
            euclideand = math.sqrt(distance)
            e_distance.append((euclideand, train[length-1])) #insert the distance and the class in the list 

            #sort the list
        e_distance.sort(key=lambda tup: tup[0]) #sort by the euclidean distance
        #get the top k elements 
        k = int(k)
        top_k = e_distance[:k]
        # print("top k\n", top_k)
        # sorted_euclidean.clear()
        # e_distance.clear()
        clist = []
        for i in top_k:
            clist.append(i[1]) #put the classes in a list to get the mode
        # print("\nclasses\n", clist)
        most = mode(clist)
        clist.clear()
        output_classes.append(most)
    
    for i in output_classes:
        print(i)



if __name__ == "__main__":
    main()
