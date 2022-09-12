from re import A


for i in range(100):
    print(i)
for i in range (10,21):
        print(i,end='x')
for i in range(1,11,2):
    print(i,end='')

    #reverse loop
for i in range (100,0,-1):
        print(i,end='')


data=[2,2,4,6,4,3,1,3,3,3,7]
for i in enumerate(data):
    print(i)

name= ['APPLE','Banana','cherry']
price= [100,40,65]
for n,p in zip (name,price):
    print(f'{n},{p}')
    


    