###wap to carecte a list of 5 names taken from user and display each name in reverse
###wap to print a fibonacci series using the concept of list(0,1,1,2,3,5,8,13...)
###wap to generate a new list that contains sqaures of each numbers for existing list x=[2,3,4,5,]=>[4,58,16,25]
### wap to generate a new list from an existing list of numbers that contains onliy odd number
### wap to generate a list by adding 2 list elementwise

#ANS1
from asyncio import PriorityQueue
from re import X


name=[]
for i in range(5):
    name. append(input("name=>"))

for name in name:
    print(name[::-1])



#ANS3
fib =[0,1]
for i in range (15):
    fib.append(fib[-1]+fib[-2])
    print(fib)

#ANS4
x=[1,2,3,3,4,5,6,7]
x2=[]
for num in x:
    x2.append(num **2)
    print(x)
    print(x2)

    
#ANS2
list_f =(0,1)
for i in range(15):
    list_f.append(fib[-1]+fib[-2])
print(list_f)

#ANS5 odd values from list
x=[1,2,3,4,5,6]
xodd=[]
for i in x:
    if i % 2 !=0:
        xodd.append(i)

print(xodd)

# add2 list elementwise
x=[1,2,3,4,5,6]
y=[6,74,3,2,1,2]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(X)
print(y)
print(z)

for i in range (1,11):
    print(f'2 * {i} = {2*i}')




