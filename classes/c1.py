#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import log3 as log

"""This is a 
        python script!"""

print("Class Basic !")

#print("=================");
class MyClass1:
    x = 5

p = "[Person]"
m = ""
#print("=================");

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(f" [{object.__class__}] [{Person.__init__.__qualname__}()] called : {self.name} is {self.age} old  ");


  def __str__(self):
    return f" [{Person.__str__.__qualname__}()] {self.name}({self.age})"

  def Print(self):
    print(f" [{Person.Print.__qualname__}()]: {self.name} is {self.age} old  ");
    self.PrintName();
    #Derived classes may override methods of their base classes. 
    #Because methods have no special privileges when calling other methods of the same object, 
    #a method of a base class that calls another method defined in the same base 
    #class may end up calling a method of a derived class that overrides it. 
    #(For C++ programmers: all methods in Python are effectively virtual.)
    #https://docs.python.org/3/tutorial/classes.html#inheritance

  def PrintName(self):
    print(f" [{Person.PrintName.__qualname__}()]: Hi! I am {self.name}  ");
    

  def Info():
    print(f" [{Person.Info.__qualname__}()]: this is a python class name Person")

#print("=================");






#print("=================");






print("=================");




































