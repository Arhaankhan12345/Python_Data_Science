#fuction2 returning value
from typing import final


def get_salary ():
    val=int(input("Enter SAlary=>"))
    fine=.09
    sal=val*fine

print("salary",get_salary())

a= get_salary()
print("salary",a)

final_salary=get_salary() + 1000
print('salary', final_salary)


def amount():
    p=(int("principle:"))
    r=float(input('rate:'))
    t=int(input('time:'))
    si = p * r * t / 100
    amt = si +p 
    return amt 

    ans = amount()
    print(f'the amount will be {ans}')
    #or this way
    print(f'the amount will be {amount()}')
    
amt, si = amount()
print(f'the amount will be {amt}on slmple interest{si}')
# or this way
print(f'the amount will be {amount()}') 


