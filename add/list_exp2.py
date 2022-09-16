books=['steelheart','firefigh','osmosis','calamity']

books.append('the final empir')
books.append('alomisc habit')
books.append('you can win')
books.append('three nistakes of my life')

print('idx/t| books')
for i,b in enumerate(books):
    print(f'{i}/t|{b}')

books[6]='the well of ascension'
books[-1]='the hero of ages'
books[2]='legion'

print('idx/t| books')
for i,b in enumerate(books):
    print(f'{i}/t|{b}')

books.insert(3,'legion:skin deep')
books.insert(5,'elantris')
print('idx/t| books')
for i,b in enumerate(books):
    print(f'{i}/t|{b}')





