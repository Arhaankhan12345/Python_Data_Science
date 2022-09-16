movise=['sholay','baghban','DDLJ','ironam','rrr','inception','mohabbate','raj','mannat']

print(len(movise))
print(movise)

movise.sort()
print(movise)

movise.reverse()
print(movise)


print('first movise',movise[0])
print('last movise',movise[-1])
print('first 3 movise',movise[:3])
print('all movise except first3',movise[3:])
print('movise with even indexes',movise[::2])
