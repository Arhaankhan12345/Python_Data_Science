
from random import randint as ri
import pgzrun
WIDTH = 800
HEIGHT = 500
 
#all the calass logic
class player(Actor):
    #override the default contructor
    def __init__(self, image,speed=5):
        pos = ri (0,WIDTH),ri(0,HEIGHT)
        super().__init__(image, pos)
        self.speed = speed
    
        
    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.x -= self.speed
        elif keyboard.D:
            self.x += self.speed 
              
    def check_boundary(self):
        if self.x <0:
            self.x =WIDTH
        if self .x> WIDTH:
            self.x =0
        if self.y > HEIGHT:
            self.y =0
        if self.y <0:
            self.y = HEIGHT

        #main gan=me code
p=player('ironman')
def draw():
    screen.fill('black')
    p.draw()

def update():
    p.move()
    p.check_boundary()





pgzrun.go()
    
        


