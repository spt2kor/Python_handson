#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import log1

"""This is a 
        python script!"""

print("testing Dictionary !")

print("=================");

# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key 
print("Accessing a element using key:") 
print(Dict['Name']) 

# accessing a element using get() 
# method 
print("Accessing 2nd D  element using get:") 
print(Dict.get(1)[2]) 

print("Accessing  element using get:") 
print(Dict.get(1)) 

print("add new element and print again  Dictionary: ")
Dict['py'] = "Python";
print(Dict);

#Dict.get(2) = "python short";
#SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?


#print(Dict[4]);  # KeyError: 4

def PrintDict(dictObj) :
    print("==================== printDict() started ");
    print(dictObj);
    print("==================== printDict() ended ");

PrintDict(Dict)

print("Creating Dictionary: dict2")


dict2 = {20 : 400 , 40 : 1600} ;
PrintDict(dict2)

print("Creating Dictionary: dict2")
Dict['nested'] = dict2;

PrintDict(Dict)
print("get nested dict value" , Dict['nested'][40])

print("Creating Dictionary: myDict")

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

print("print using module function ")
log1.PrintDict(myDict)

print("=================");







# https://www.geeksforgeeks.org/python-data-structures/