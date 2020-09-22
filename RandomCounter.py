# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:27:03 2020

@author: fasa
"""

# import the random library for use the 
# function random.randint
import random
#import numpy as np

def generateRandomNumbers(count, maxNumber):
    
  
    listRandomNr = []
    
    maxNumber   = int(maxNumber) # Convert string to int (integer)
    count       = int(count)     # dito
  
    for i in range(0 ,count):
        nr = random.randint(1, maxNumber)
        listRandomNr.append(nr)
        
    return listRandomNr


def frequencyOfNumbers(matrix):
    
    counter = 0
    lastcounter = 0
    result = ''
    
    for n in matrix:
        counter = 0
        for x in matrix:
            if n == x:
                counter = counter + 1
                if counter > 1:
                    if counter > lastcounter :
                        lastcounter = counter
                        result =  "Die Zahl " + str(x) + " hat die höchste frequenz von " + str(counter)
                
            
                     
    return result                     


randomCounter = input("Wie viele Zufallszahlen sollen generiert werden: ")
randomRange = input("Gebe die höchste Zahl an: ")

liste = generateRandomNumbers(randomCounter, randomRange)

print(liste)
frequenzy =  frequencyOfNumbers(liste)
print(frequenzy)
