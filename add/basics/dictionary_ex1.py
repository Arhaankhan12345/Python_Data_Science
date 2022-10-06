from pprint import pprint
from tkinter.tix import Form


my_dis={1:'apple',2:'ball'}

val = ['Rajendera singh',30, 10, 'account','staff officer',60000,7,]

val_dist ={
    'employe':'rajendra singh', 'age': 30,'experience':10, 'dep': 'accounts',
    'designation': 'system officer', 'salary':600000, 'team_size': 7 
 }

# displaying a dict
print(val_dist)

#rwtreival of value
ans=val_dist['desingnation'] #key in sqr brackets
print(ans)
print(val_dist['salary']) #correct
print(val_dist['experience']) #incorrect

# adding a data inside dict
val_dist['company'] ='acme.inc'

print(val_dist)

from pprint import pp

pp(val_dist)




