
from tkinter.font import names


nums =[1,2,3,4,1,2,3,4,5,6,7,3,3,5,6,]
names['ajay singh','vijay partap','gunja thakur']


num_sqr = map(lambda i:1** 2, nums)
print(num_sqr)

num_sqr1 = list(map(lambda i: i+4 i**2, nums))
print(num_sqr1)
first_names = tuple(map(lambda nm: nm.split()[0], names))
print(first_names)