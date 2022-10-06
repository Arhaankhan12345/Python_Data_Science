# TUPLE FUCTION

#COUNT
from operator import index


x = (1,2,3,1,2,3,1,2,3,1,1,1,3,3,3,2,2,2,)
print('3occurs=',x.count(3))
print('5occurs=',x.count(5))
print('1occurs',x.count(1))
print('2occurs',x.count(2))
#INDEX
Y=(34,76,88,45,13,23,34)
print('34 is at =',Y.index(34,1),'place')#when sam number multiple time only first time index is print but second index

print('45 is at =',Y.index(45),'place')#y.index (SRCH_ELEMENT,star value)
print('13 is at =',Y.index(13),'place')