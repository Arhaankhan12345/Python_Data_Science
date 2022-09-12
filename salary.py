name=str(input("Enter ur name"))
bsal=int(input("Enter ur salary"))

if bsal>100000:
    da=(bsal*0.035)
    hra=(bsal*0.091)
elif bsal>80000:
    da=(bsal*0.032)
    hra=(bsal*0.090)
elif bsal>60000:
    da=(bsal*0.028)
    hra=(bsal*0.090)
elif bsal>50000:
    da=(bsal*0.025)
    hra=(bsal*0.080)
elif bsal>40000:
    da=(bsal*0.025)
    hra=(bsal*0.077)
elif bsal>30000:
    da=(bsal*0.022)
    hra=(bsal*0.080)
elif bsal>20000:
    da=(bsal*0.022)
    hra=(bsal*0.070)
else:
    da=(bsal*0.022)
    hra=(bsal*0.060)

fsal=bsal+da+hra
print("Your Final Salary is =",fsal)
print("Your DA is= ",da)
print("Your HRA is =",hra)

