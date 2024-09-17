#!/opt/python/3.11/bin/python
# -*- coding: utf-8 -*-

"""This is a 
        python script! for Logs2"""

print("Loading reusable Logs2 !")

import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..' )
sys.path.append( mymodule_dir )
#for p in sys.path:
#    print( p )

import log1 as log

# https://csatlas.com/python-import-file-module/