from random import randint

def hello():
    print("HOLA")
    print("AMIGOS")
    print('✋✋✋')

def roll_dice():
   dices =['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
   print("=>",dices[randint(1,6)])

#call
#hello()
#hello()
#hello()

roll_dice()
roll_dice()
roll_dice()