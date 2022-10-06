
#making a set
my_set={1,2,3,2,5,} #wil not show repiting values
print(my_set)

#set from list
list_x=[1,2,3,3,4,5,6]
my_set=set(list_x)
print(my_set)
print(type(my_set))

#error due to mutable entry
my_set={1,2[3,4]}              #unhachable type list error

# creting empty set
a =set()       # use of set fuction for blank set
print(type(a))      

#modify set
my_set= {1,2}
print("original set was =",my_set)

#adding eliment
my_set.add(2)       ## add fuction to add 1 value 1 time
print("affter adding 2 to it =",my_set)
#add multipal values 
my_set.update([2,3,4,5,6,])
print("after updeting multipal valuse=",my_set)

#add multipal vlues from diffrent entities
my_set.update([3,8,9],{1,6,10,45})
print("final set is =",my_set)

#Removing item form set
#using discard and remove function 
n_set={1,2,3,4,5,6,}
print(n_set)

#removal by  discard fuction 
n_set.discard(4)
print(n_set)

#removal by  discard fuction (same as discard ) but if list eliment nat present program crash
n_set.remove(6)
print(n_set)

#pop function (removes random eliment )
n_set.pop()
print(n_set)

#clere fuction to clean entire set at once 
n_set.clear()
print(n_set)