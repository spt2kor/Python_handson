#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import log1

"""This is a 
        python script!"""

print("testing Dictionary !")

print("=================");

print("=================");




def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print("=================");

def my_function1(child3, child2, child1):
  print("The youngest child is " + child3)

my_function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print("=================");


def my_function2(**kid):
  print("His last name is " + kid["lname"])

my_function2(fname = "Tobias", lname = "Refsnes")


print("=================");



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


print("=================");






print("=================");

#https://www.w3schools.com/python/python_functions.asp

































