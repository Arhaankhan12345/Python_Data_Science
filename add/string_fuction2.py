from importlib.resources import contents
from unicodedata import name


msg = "we will be seeing the horizon"

word = msg.split()
print(word)


word = msg.split('e')
print(word)

#replace()
updated_ms= msg.replace('seeing','viewing')
print(updated_ms)

updated_ms= msg.replace('e','')
print(updated_ms)

#join()
path =['user','mypc','document','date','file.tax']

contents="/".join(path)
print(contents)

#strip()
name ="   stev   "
cleaned_name = name.strip()
print(cleaned_name)
print(len(name),len(cleaned_name))

msg2= '''
we are venom
'''

cleaned_msg2 = msg2.strip()
print(cleaned_msg2)
print(len(msg2),len(cleaned_msg2))

from helper import read
data= read('pride_n_prejuice.tax')
#wap to fine frequency of all the vowels in the 'data

for vowel in 'aeiou':
    print(f"{vowel}=> {data.lower().count(vowel)}times")

#wap to remove all the punctuation from the string
str='he@11%!@&*(!@wo!@r,l!d)'
from string import punctuation
for p in punctuation:
    str=str.replace(p,'')
print(str)






