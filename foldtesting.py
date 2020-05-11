import sys
import os
import csv
import math 
from statistics import *

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

    if "NB" in algorithm:
        NB(training, testing)

def kNN(k, training, testing): #open files see if i need to extract the first column out 
    # testing_file = open(testing, "r" )
    # training_file = open(training, "r")
    output_classes = []

    training_array = []
    if os.path.exists(training):
        with open(training) as File2:
            for row in csv.reader(File2, delimiter= ','):
                training_array.append(row) #the length of each entry tells us how many columns there are 

    testing_array = []
    if os.path.exists(testing):
        with open(testing) as File:
            for row in csv.reader(File, delimiter= ','):
                testing_array.append(row) #the length of each entry tells us how many columns there are 

    #classification compare with new value with ever training example
    #calculate the euclidean distance
    for test in testing_array: #one row in the testing dataset
        e_distance = [] 
        for train in training_array: #go through all the rows in the training dataset
            length = len(test) # train = n+ 1 with class column and test = n should have the same length
            distance = 0.0
            for n in range(0, length): # going through all the elements to get the euclidean distance
                d = (float(train[n]) - float(test[n])) ** 2 #square the differnce 
                distance = distance + d
            
            euclideand = math.sqrt(distance)
            e_distance.append((euclideand, train[length])) #insert the distance and the class in the list 

        #sort the list
        e_distance.sort(key=lambda tup: tup[0]) #sort by the euclidean distance
        #get the top k elements 
        k = int(k)
        top_k = e_distance[:k]
        clist = []
       
        for i in top_k:
            clist.append(i[1]) #put the classes in a list to get the mode
        # print(clist)
        try:
            most = mode(clist)
            clist.clear()
            output_classes.append(most)
        except StatisticsError as e:
            output_classes.append("yes")
            clist.clear()
        
    
    for i in output_classes:
        print(i)
    

def NB(training, testing): 
    output_classes = []

    training_array = []
    if os.path.exists(training):
        with open(training) as File2:
            for row in csv.reader(File2, delimiter= ','):
                training_array.append(row) #the length of each entry tells us how many columns there are 


    testing_array = []
    if os.path.exists(testing):
        with open(testing) as File:
            for row in csv.reader(File, delimiter= ','):
                testing_array.append(row) #the length of each entry tells us how many columns there are 
 
    yesarraydata = []
    noarraydata = []
    yessummary = []
    nosummary = []
    output_classes = []
    #separation by class
    for row in training_array:
        length = len(row)
        if "yes" in row[length-1]:
            yesarraydata.append(row)
        else:
            noarraydata.append(row)

    yessummary = dataset_stat(yesarraydata)
    nosummary = dataset_stat(noarraydata)
   
    [x1,x2] = probyesandno(yesarraydata,noarraydata,training_array)
    for row in testing_array:     
        Pyes = calculateclassprob(row,yessummary,length,yesarraydata,training_array)
        Pno = calculateclassprob(row,nosummary,length,noarraydata,training_array)
        if Pyes >= Pno:
            output_classes.append("yes")
        else:
            output_classes.append("no")

    for i in output_classes:
        print(i)            

def meann(columnarray):
    if "yes" in columnarray or "no" in columnarray:
        pass
    else:
        columnarrayf = [float(i) for i in columnarray]
        return mean(columnarrayf)

def stdf(columnarray):
    if "yes" in columnarray or "no" in columnarray:
        pass   
    else:
        columnarrayf = [float(i) for i in columnarray]
        return stdev(columnarrayf)

def dataset_stat (arraydata):
    summary = [(meann(column), stdf(column), len(column)) for column in zip(*arraydata)]
    #make column
    return summary

def probdensityfunction (x, mean, std):
    x = float(x)
    if std != 0:
        return (1 / (std*math.sqrt(2 * math.pi))) * math.exp(-((x-mean)**2 / (2 * std**2 )))
    else:
        return 100

def calculateclassprob (arraydata,summary,length,yesnoarray,trainingarray):
    x = len(yesnoarray)/len(trainingarray)
    probability = x
    a = 0
    for i in arraydata:
        mean, std, lenn = summary[a]
        probability *= probdensityfunction(i,mean,std)
        a = a +1
    return probability

def probyesandno (yesarraydata,noarraydata,trainingdata):
    pyesandno = []
    x = len(yesarraydata)/len(trainingdata)
    y = len(noarraydata)/len(trainingdata)
    return x,y


if __name__ == "__main__":
    main()