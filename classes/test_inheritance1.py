#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import log3 as log
import inheritance1 as INH
"""This is a 
        python script!"""

print("testing Classes Inheritance1.py !")

print("================= p1 = INH.Class.Person(\"Pyoro\" , 33)");
p1 = INH.Class.Person("Pyoro" , 33)
print("=================   p1.Print()   ");
p1.Print()  

print("=================   s1 = INH.Student(\"Samsung\" , 30)  ");
s1 = INH.Student("Samsung" , 30)
print("=================   s1.Print()  ");
s1.Print()  
print("=================   s1.PrintName()  ");
s1.PrintName()  

#s2 = INH.Student() #TypeError: Person.__init__() missing 2 required positional arguments: 'name' and 'age'
#s2.Print()  

print("=================  s2 = INH.Student1(\"Eye\" , \"Bird\" , 40)  ");
s2 = INH.Student1("Eye" , "Bird" , 40)
print("=================  s2.PrintFullName()  ");
s2.PrintFullName()
print("=================  s2.Print()  ");
s2.Print();
    #Derived classes may override methods of their base classes. 
    #Because methods have no special privileges when calling other methods of the same object, 
    #a method of a base class that calls another method defined in the same base 
    #class may end up calling a method of a derived class that overrides it. 
    #(For C++ programmers: all methods in Python are effectively virtual.)
    #https://docs.python.org/3/tutorial/classes.html#inheritance
print("=================  s2.PrintName()  ");
s2.PrintName();  
print("=================  print(s2)  ");
print(s2);  
print("=================  INH.Student1.Info();  ");
INH.Student1.Info();
print("=================  isinstance( s2 , INH.Student1);  ")  ;
print ( f" isinstance( s2 , INH.Student1) : {isinstance( s2 , INH.Student1)}" );
print ( f" isinstance( s2 , INH.Student) : {isinstance( s2 , INH.Student)}" );
print ( f" isinstance( s2 , INH.Class.Person) : {isinstance( s2 , INH.Class.Person )}" );
print ( f" isinstance( s2 , object) : {isinstance( s2 , object )}" );

print ( f" isinstance( p1 , INH.Student1) : {isinstance( p1 , INH.Student1)}" );

print("================= issubclass( INH.Student1 , INH.Class.Person)  ");

print ( f" issubclass( INH.Student1 , INH.Class.Person) : {  issubclass( INH.Student1 , INH.Class.Person) }" );
print ( f" issubclass( INH.Student , INH.Class.Person) : {  issubclass( INH.Student , INH.Class.Person) }" );
print ( f" issubclass( INH.Student1 , object) : {  issubclass( INH.Student1 , object) }" );
print ( f" issubclass( int , object) : {   issubclass( int , object) }" );

print ( f" issubclass( INH.Student1 , INH.Student) : {  issubclass( INH.Student1 , INH.Student)  }" );
print ( f" issubclass( INH.Student , INH.Student1) : {  issubclass( INH.Student , INH.Student1)  }" );
print("=================");



print("=================");