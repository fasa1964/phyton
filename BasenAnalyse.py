# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:31:03 2020

@author: fasa
"""

# Aufgabe das Zählen und Berechnen der Häufigkeit 
# einzelner Sequenzen




Sequenz = input("Sequenz:")
control_base = input("Die zu kontrollierende Base:")


def basen_counter(Sequenz):
    
    base = 0
    
    for i in Sequenz:
        if i == control_base:
            base = base + 1
            
    return base


def basen_percent(Sequenz):
    
    base = 0
    
    for i in Sequenz:
        if i == control_base:
            base = base + 1
            
    p = base / len(Sequenz)*100
    
    return p


print ("Die Anzahl von", control_base, "in der Sequenz beträgt:" ,basen_counter(Sequenz))
print ("Der Gehalt von", control_base, "in der Sequenz beträgt:" ,basen_percent(Sequenz), "%")

    