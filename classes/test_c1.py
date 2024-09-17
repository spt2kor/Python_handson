#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import log3 as log
import c1 as Class
"""This is a 
        python script!"""

print("testing class basic c1.py !")

print("=================");
cObj1 = Class.MyClass1();
print ( cObj1.x )
print ( cObj1 )
print ( Class )
#print ( c1 )           NameError: name 'c1' is not defined
print ( Class.MyClass1 )

print("=================");
print ( cObj1.x )
p1 = Class.Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)
print(Class.Person)
p1.Print()

print("=================");
p2 = Class.Person("Snow", 60)
print(p2)
p2.Print();

print("=================");
del p1.age;
p2.Print()
# p1.Print() #AttributeError: 'Person' object has no attribute 'age'

del p1;
# print(p1) #NameError: name 'p1' is not defined. Did you mean: 'p2'?

print("=================");
#p2.Info()  #TypeError: Person.Info() takes 0 positional arguments but 1 was given
Class.Person.Info()
print("=================");


print("=================");

#https://www.w3schools.com/python/python_classes.asp


































