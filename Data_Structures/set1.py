#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-
import log1 as log
"""This is a 
        python script!"""

print("testing Set !")

print("=================");

# Creating a Set with  
# a mixed type of values 
# (Having numbers and strings) 
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with the use of Mixed Values") 
print(Set) 
 
# Accessing element using 
# for loop 
print("\nElements of set: ") 
for i in Set: 
    print(i, end =" ") 
print()
 
# Checking the element 
# using in keyword 
print("Geeks" in Set)

log.PrintSet(Set)
print("=================");







# https://www.geeksforgeeks.org/python-data-structures/