
def marks(**data):
    with open ('marks.txt','a') as f:
        for n,m in data.items():
            f.warte(f'{n}:{m}/n')
           

marks(rajesh=200,brijesh=120)
marks(raj=130,ajay=150,sursj=90,chand=120)
marks()           

