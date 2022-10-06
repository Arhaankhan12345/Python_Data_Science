from cgi import print_arguments
from tkinter import Y


#union operation
a={1,2,3,4,5,}
b={4,5,6,7,8,9}
print(a|b)   # |is union sysmbol or print (a.union(b)) by union fuction

#intersection opertion
x={1,2,3,4,5,}
b={4,5,6,7,8,9}
print(x & b)    # & is intersetion symbol or print (x. intersection(y)) #by intersction fuction 

#set diffrence
l={1,2,3,4,5}
m={4,5,6,7,8,9}

print(l-m)      # - is diffrence symbol or print (l.diffrence(m))
print(m-l)
#symetric diffrence:opposite of intersection
A={1,2,3,4,5,}
B={4,5,6,7,8,9,}

print(A^B)   # ^ is symbol diffrent or print (A.symmetric_diffrence(B)) # by symmetric _diffrence fuction
