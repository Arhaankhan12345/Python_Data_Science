
x = [1,2,3,1,2,2,3,3,1,1,2,3,3,3,1,1,1,2,3,3,3,1,4,1,1,2,2,2]


x_one= x.count(1)
x_two= x.count(2)
x_four= x.count(4)
x_five= x.count(5)
print('1 occuurred',x_one,'times')
print('2occuurred',x_two,'times')
print('4occurred',x_four,'times')
print('5occurred',x_five,'timse')

y=[23,45,67,6,7,8,21,32,43]
z=[12,2,3,4,5,6,1]

print('x adding y')
x.extend(y)
print(x)
print('x adding z')
x.extend(z)
print(x)
xyz =x + y + z
print(xyz)
a=['apple','banana','cherry','dragonfrutit','elaichi']
v=a.pop(3) # pop can remove value form on index (delet)
print(a)
print(v)
lv=a.pop() #pop remove last value by default
print(a)
print(lv)


















