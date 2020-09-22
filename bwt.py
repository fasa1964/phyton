# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:33:50 2020

@author: fasa

"""

# 


# Always the first charater 
START_CHAR ='$'


def inverse(string):
    length = len(string)
    table = ['' for x in range(length)]

    for j in range(length):
        for i in range(length):
            table[i] = string[i] + table[i]
        table = sorted(table)

        
    #print("Inverse funktion", table[0])
    reverseString = table[0]
    liste =  reverseString.split(START_CHAR)
    reverseString = liste[-1]
    
    return reverseString 

# Transform the input text into a sorted matrix
def transform(string):
    
    # Add a $ - Char to keep the first charater 
    string = '{}{}'.format(START_CHAR, string)
    length = len(string)
    
    # Create an empty matrix 
    matrix = []
    
    
    # Rotate the string form right to left
    # and insert into th matrix
    for i in range(length):
        rotated = string[i:] + string[:i]
        matrix.append(rotated)

    # Sort the matrix alphabetically
    matrix = sorted( matrix )

    return matrix
# End of function
  
# Get last character from all sequenz
def transformSequenz(liste):
    
    lastSequenz = ""
    
    lastSequenz = ''.join([x[-1] for x in liste])
    return lastSequenz


# Input text to transform  
text = input("Eingabe: ")

# Calls function and returned sorted matrix
table = transform(text) 

# Output matrix on console
print("1. Transformed sorted matrix: \n", table)

lastSequenz = transformSequenz(table)

# Output last element from matrix table
print("2. Transformed text: ", lastSequenz )  

invers_text = inverse( lastSequenz )
print("3. retransformed text: ", invers_text )  

 
