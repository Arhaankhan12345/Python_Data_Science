


email= input ("Enter ur email=>")
if '@' in email:
    if len(email) >=11:
        if '.com'in email or 'org'in email:
            print("your email look valid")
        else:
            print('invalide  domasin')
else:
    print('your email dose not have @')
        
    
            

