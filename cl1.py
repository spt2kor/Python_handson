#!/opt/python/3.11/bin/python


print("=================");



import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'alpha', 'beta' )
sys.path.append( mymodule_dir )
for p in sys.path:
    print( p )



#import sys

#for p in sys.path:
#    print( p )

print("=================");








































