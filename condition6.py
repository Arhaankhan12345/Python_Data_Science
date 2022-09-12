email= input ("Enter ur email=>")

if '@' in email:
    print('your email dose not have @')
elif len(email)<11:
    print('length of email not vail')
elif'.com' not in email and '.not'a email:
    print('invail domain ')
else:
    print('your email look valid')