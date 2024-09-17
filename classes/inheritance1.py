#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

import log3 as log
import c1 as Class
#import c1.Person as Person    #ModuleNotFoundError: No module named 'c1.Person'; 'c1' is not a package

"""This is a 
        python script!"""

print("Class Inheritance 1 !")

print("=================");



#=======================================

class Student(Class.Person):
    pass


class Student1(Student):
    def __init__(self , name , surname , age ):
        Student.__init__(self,name,age)
        self.surname = surname
        print(f" [{Student1.__init__.__qualname__}()] called : {self.surname}, {self.name} is {self.age} old  ");

    def PrintFullName(self ):
        print(f" [{Student1.PrintFullName.__qualname__}()] {self.surname},{self.name} is {self.age} old")

    def PrintName(self):
        super().PrintName();
        print(f" [{Student1.PrintName.__qualname__}()] Hi! I am {self.name} {self.surname} ");

    def __str__(self):
        return f" [{Student1.__str__.__qualname__}()] {self.name}({self.age})"

    def Info():
        print(f" [{Student1.Info.__qualname__}()]: this is a python class name Student1")