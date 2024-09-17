#!/opt/python/3.11/bin/python

l = [1,4,9,16,25];
print(l);

#print l[2:4];
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

print ( l[2:4]);

l[0] = 100;

print(l);
print( "len(l)" , len(l) );

l = [];
print(l);


print("=================");

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)

print( x[0]);

print(x[0][1])

print("=================for - Iterator");
l = [1,4,9,16,25];

for no in l:
    print (no);

print("================= Iterator");

itr = iter(l)

print (next(itr))
print (next(itr))

for i in range(2,5):
    print (i, "\t" , next(itr))
else:
    print(i, " \t " ,  "range of list is over")




#https://www.w3schools.com/python/python_for_loops.asp
#https://www.w3schools.com/python/python_iterators.asp































