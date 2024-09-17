#!/opt/python/3.11/bin/python


print("================= for loop ");

#lst1 = [ range(2,100,5) ]
lst1 = list(  range(2,50,5) )
print( lst1)

print("=================");

for x in lst1 :
    print(x)

print("list length:", len(lst1))
print("=================");
for i in range (0,len(lst1)) :
    
    if(i == 5):
        break
    elif (i %2 == 0):
        print (f"even : {i } value is   { lst1[i] } ")
    elif (i%3 == 0) :
        continue
    else:
        print (f"{i } value is   { lst1[i] } ")
else:
    print(f"loop ends at {i} index , {lst1[i] }")

print("=================");

itr = iter(lst1)

for i in range(0,len(lst1)):
    print (f" value at {i} is {next(itr)}")
else:
    print(f"loop ends at {i} index , {lst1[i] }")



#https://www.geeksforgeeks.org/range-to-a-list-in-python/

#https://www.w3schools.com/python/python_iterators.asp

#https://docs.python.org/3/tutorial/classes.html

































