from typing import Counter
from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

for letter in ascii_lowercase:
    Counter = data.count(letter)
    print(f'{letter} found {Counter}times')


#wap to find tha most occring alphabet and its frequency

feeq=0
freq_letter =''
for letter in ascii_lowercase:
    Counter= data.count(letter)
    print


