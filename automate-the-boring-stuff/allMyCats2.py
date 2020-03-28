# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:35:05 2020

allMyCats2 from 'Automate the boring stuff'
"""


catNames = []
while True:
    print('Enter the name of cat '+ str(len(catNames)+1)+ ' (or enter nothing to stop.):')
    name = input()
    if name =='':
        break
    catNames.append(name) #changed concatenate to append method

print('The cat names are ' + ", ".join(catNames[0:len(catNames)-1])+", and " + catNames[-1]) # changed loop to join method
