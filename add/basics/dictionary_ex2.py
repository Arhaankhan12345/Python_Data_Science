from pprint import pp
from re import S

movies ={}
movies['top gun: maverick']=8.3
movies['everything everywhwre all at once']=8.1
movies['spider-man: no way home']=8.2

pp(movies)

for item in movies:
    print(item)

    print('only values')
    for item in movies:
        print(movies[item])

    print('both key and values')
    for key in movies:
        print(key,movies[key])
       


# user  input
for i in range (3):
    name = input ("movis name:")
    rating = float(input('movie rating: ')) 
    movies[name]=rating

    print('using disct.items() method')
    for k,v in movies.items():
        print(k,v)
    