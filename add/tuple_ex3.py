#tuple-set-list(interchangeable)
x=tuple[1,2,3,4,5,6,6,7]
xt=tuple(x) #list-tuple
xl=list(xt) #tuple-list
xs=set(x)   #list-set
x=list(xs)  #set-list
xs=set(xt)  #tuple-set
xt=tuple(xs) #set-tuple

print(type(x))
print(type(xt))
print(type(xl))
print(type(xs))

#wap to create a tuple, by tacking ten inputs form the user
x=[]
r=int(input("enter range="))
for i in range(r):
    var=int(input("Enter renge="))
    x.append(var)

t=tuple (x)
print(type(t))
print(t)