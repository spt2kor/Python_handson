#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-
import log1 as log
"""This is a 
        python script!"""

print("testing Frozen Set !")

print("=================");

# Same as {"a", "b","c"}
normal_set = set(["a", "b","c"])
 
print("Normal Set")
print(normal_set)
 
# A frozen set
frozen_set = frozenset(["e", "f", "g"])
 
print("\nFrozen Set")
print(frozen_set)
 
# Uncommenting below line would cause error as
# we are trying to add element to a frozen set

#frozen_set.add("h")   #AttributeError: 'frozenset' object has no attribute 'add'


log.PrintSet(frozen_set)
print("=================");







# https://www.geeksforgeeks.org/python-data-structures/