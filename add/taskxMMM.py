import math
x=[2,2,3,3,1,2,3,4,5,6]
print("sum",sum(x))
print("mean=>",sum(x)/len(x))
x.sort()
if len(x) % 2 == 0:
    idx = len (x)//2
    value = x[idx] + x [idx+1]
    print("median=>",value/2)
else: 
    value = x[len(x)//2 + 1]
    print("median=>",value/2) 

    