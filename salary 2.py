from email.mime import base


name=str(input("Enter ur name"))
bsal=int(input("Enter ur salary"))

if bsal>900000:
    da=(bsal*0.045)
    hra=(bsal*0.081)
elif bsal>70000:
    da=(bsal*0.042)
    hra=(bsal*0.80)
elif bsal>65000:
    da=(bsal*0.025)
    hra=(bsal*0.075)
elif bsal>55000:
    da=(bsal*0.035)
    hra=(bsal*0.075)
elif bsal>50000:
    da=(bsal*0.032)
    hra=(bsal*0.066)
elif bsal>350000:
    da=(bsal*0.035)
    hra=(bsal*0.065)
elif bsal>25000:
    da=(bsal*0.022)
    hra=(bsal*0.55)
else:
    da=(bsal*0.02)
    hra=(bsal*0.05)

    
fsal=bsal+da+hra
print("Your Final Salary is =",fsal)
print("your da is=",da)
print("your hra is=",hra)
