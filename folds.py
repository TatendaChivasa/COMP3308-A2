# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:43:16 2020 fuck it crashed a minute a go and now I have 
to do it all over again fck :'v'
"""

import sys
import os
import csv
import math 
from statistics import mode
from math import sqrt
from statistics import mean



def main():
    training = sys.argv[1]

    training_array = []
    if os.path.exists(training):
        with open(training) as File2:
            for row in csv.reader(File2, delimiter= ','):
                training_array.append(row)

    noarraydata = []
    yesarraydata = []
    for row in training_array:
        length = len(row)
        if row[length-1] == "yes":
            yesarraydata.append(row)
        else:
            noarraydata.append(row)

    A = int(len(yesarraydata)/10) #500\10 = 50
    B = int(len(noarraydata)/10)   #268\10
    leftovers = (len(yesarraydata)+ len(noarraydata))-((A+B)*10)
    fold = A + B 
    #print(A)
    #print(B)
    #print(fold)
    counter1 = 0
    f1yes= 0
    f2yes=0
    f3yes=0
    f4yes=0
    f5yes=0
    f6yes=0
    f7yes=0
    f8yes=0
    f9yes=0
    f10yes=0
    f1no=0
    f2no=0
    f3no=0
    f4no=0
    f5no=0
    f6no=0
    f7no=0
    f8no=0
    f9no=0
    f10no=0
    fold1 = []
    fold2= []
    fold3= []
    fold4=[]
    fold5= []
    fold6=[]
    fold7=[]
    fold8=[]
    fold9=[]
    fold10 =[]
    count = 0
    for row in training_array:
        
        if row[length-1] == "yes" and counter1<fold and f1yes<(A-1):
            
            fold1.append(row)
            counter1 = counter1 + 1
            f1yes = f1yes + 1
            # training_array.pop(count)
        elif row[length-1] == "no" and counter1<fold and f1no<(B-1):
            fold1.append(row)        
            counter1 = counter1 + 1
            f1no = f1no + 1
            # training_array.pop(count)
#FOLD2            
        if row[length-1] == "yes" and counter1>=76 and counter1<(152) and f2yes<(A):
            
            fold2.append(row)
            counter1 = counter1 + 1
            f2yes = f2yes + 1 
            # training_array.pop(count)       
        elif row[length-1] == "no" and counter1>=fold and counter1<(fold*2) and f2no<(B):
            
            fold2.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f2no = f2no + 1            
#FOLD3        
        if row[length-1] == "yes" and counter1>=(fold*2) and counter1<(fold*3) and f3yes<(A):
            
            fold3.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f3yes = f3yes + 1
        elif row[length-1] == "no" and counter1>=(fold*2) and counter1<(fold*3) and f3no<(B):
            
            fold3.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f3no = f3no + 1
#FOLD4            
        if row[length-1] == "yes" and counter1>=(fold*3) and counter1<(fold*4) and f4yes<(A):
            
            fold4.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f4yes = f4yes + 1
        elif row[length-1] == "no" and counter1>=(fold*3) and counter1<(fold*4) and f4no<(B):
            
            fold4.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f4no = f4no + 1
#FOLD5            
        if row[length-1] == "yes" and counter1>=(fold*4) and counter1<(fold*5) and f5yes<(A):
            
            fold5.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f5yes = f5yes + 1
        elif row[length-1] == "no" and counter1>=(fold*4) and counter1<(fold*5) and f5no<(B):
            
            fold5.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f5no = f5no + 1 
#FOLD6            
        if row[length-1] == "yes" and counter1>=(fold*5) and counter1<(fold*6) and f6yes<(A):
            
            fold6.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f6yes = f6yes + 1
        elif row[length-1] == "no" and counter1>=(fold*5) and counter1<(fold*6) and f6no<(B):
            
            fold6.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f6no = f6no + 1
#FOLD7            
        if row[length-1] == "yes" and counter1>=(fold*6) and counter1<(fold*7) and f7yes<(A):
            
            fold7.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f7yes = f7yes + 1
        elif row[length-1] == "no" and counter1>=(fold*6) and counter1<(fold*7) and f7no<(B):
            
            fold7.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f7no = f7no + 1 
#FOLD8            
        if row[length-1] == "yes" and counter1>=(fold*7) and counter1<(fold*8) and f8yes<(A):
            
            fold8.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f8yes = f8yes + 1
        elif row[length-1] == "no" and counter1>=(fold*7) and counter1<(fold*8) and f8no<(B):
            
            fold8.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f8no = f8no + 1
#FOLD9            
        if row[length-1] == "yes" and counter1>=(fold*8) and counter1<(fold*9) and f9yes<(A):
            
            fold9.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f9yes = f9yes + 1
        elif row[length-1] == "no" and counter1>=(fold*8) and counter1<(fold*9) and f9no<(B):
            
            fold9.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f9no = f9no + 1
#FOLD10            
        if row[length-1] == "yes" and counter1>=(fold*9) and counter1<(fold*10) and f10yes<(A-1):
            
            fold10.append(row)
            counter1 = counter1 + 1
            # training_array.pop(count)
            f10yes = f10yes + 1
        elif row[length-1] == "no" and counter1>=(fold*9) and counter1<(fold*10) and f10no<(B-1):
            
            fold10.append(row)        
            counter1 = counter1 + 1
            # training_array.pop(count)
            f10no = f10no + 1  
        count += 1
    i = (A+B)*10 #760
    i2 = 1  
    i3 =0
    newarray = []
    newarray = training_array[i:]

    # for leftoverrow in newarray:
    #     if i3 == 0:
    #         fold1.append(leftoverrow)
    #         i3 = i3 + 1
    #     elif i3 == 1:
    #         fold2.append(leftoverrow)
    #         i3 = i3 + 1
    #     elif i3 == 2:
    #         fold3.append(leftoverrow)
    #         i3 = i3 + 1 
    #     elif i3 == 3:
    #         fold4.append(leftoverrow)
    #         i3 = i3 + 1 
    #     elif i3 == 4:
    #         fold5.append(leftoverrow)
    #         i3 = i3 + 1
    #     elif i3 == 5:
    #         fold6.append(leftoverrow)
    #         i3 = i3 + 1 
    #     elif i3 == 6:
    #         fold7.append(leftoverrow)
    #         i3 = i3 + 1 
    #     elif i3 == 7:
    #         fold8.append(leftoverrow)
    #         i3 = i3 + 1
    #     elif i3 == 8:
    #         fold9.append(leftoverrow)
    #         i3 = i3 + 1 
    #     elif i3 == 9:
    #         fold10.append(leftoverrow)
    #         i3 = i3 + 1

    print("fold1")
    # print(fold1)
    countno1 = 0 
    countyes1= 0
    for i in fold1:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)

    print("fold2")
    # print(fold2)
    countno1w = 0 
    countyes1w= 0
    for e in fold2:
        l = len(e)
        print(*e, sep = ",")
        if e[l-1] == "yes":
            countyes1w += 1
        else:
            countno1w += 1
    print("\n")
    print("number of nos ", countno1w)
    print("number of yes ", countyes1w)

    print("fold3")
    # print(fold3)
    countno12 = 0 
    countyes12= 0
    for i in fold3:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes12 += 1
        else:
            countno12 += 1
    print("\n")
    print("number of nos ", countno12)
    print("number of yes ", countyes12)

    print("fold4")
    # print(fold4)
    countno1 = 0 
    countyes1= 0
    for a in fold4:
        l = len(a)
        print(*a, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)

    print("fold5")
    # print(fold5)
    countno1 = 0 
    countyes1= 0
    for i in fold5:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)

    print("fold6")
    # print(fold6)
    countno1 = 0 
    countyes1= 0
    for i in fold6:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)

    print("fold7")
    # print(fold7)
    countno1 = 0 
    countyes1= 0
    for i in fold7:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)

    print("fold8")
    # print(fold8)
    countno1 = 0 
    countyes1= 0
    for i in fold8:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)

    print("fold9")
    # print(fold9)
    countno1 = 0 
    countyes1= 0
    for i in fold9:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)

    print("fold10")
    # print(fold10)
    countno1 = 0 
    countyes1= 0
    for i in fold10:
        l = len(i)
        print(*i, sep = ",")
        if i[l-1] == "yes":
            countyes1 += 1
        else:
            countno1 += 1
    print("\n")
    print("number of nos ", countno1)
    print("number of yes ", countyes1)


if __name__ == "__main__":
    main()