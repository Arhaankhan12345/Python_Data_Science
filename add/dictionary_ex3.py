from audioop import reverse
import helper as h
from string import punctuation
data = h.read ('basics/pride_prejudice.txt')
print(len(data))


#remove punctuation
print("PUNC", punctuation)
for p in punctuation:
    data= data.replace(p,'')

    #split into word and remove spaces and empty string
    words= [word.strip() for word in data.lower().split()]
    print("TOTAL WORDS FOUND:",len(words))
    print("UNIQUE WORD FOUND:", len(set(words)))

    # crecte a distionary
    wc = {}
    for word in set(word):
        wc[word] = words.count(word)
        


    #sorting the dictionary -> wc.items()returan a list of tuple 
    wc = sorted(wc.item(), key=lambda x: x[1], reverse=True)

    # Print the top 10 words 
for i in range(10):
    print(wc(i))

    # word cloud
    from wordcloud import wordcloud
    import matplotlib.pyplot as plt

    #crecte a string with all the word
    tex =''.joine(words)

