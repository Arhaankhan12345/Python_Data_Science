
import pgzrun 

HEIGHT = 600
WIDTH = 1000
c = Actor('chick',(100,100))
w=  Actor('walrus',(400,400))
cookie=Actor('coo')
speed = 3
def draw():
   
    Screen.blit ('bg',pos=(0,0))
    c.draw()
    w.draw()
screen.draw.text("A chicken story"(10,10), color='red')
screen.draw.text(f"score:{score}",(900,10),color='red')
cookie.draw()

def update():
    global score
    if keyboard.w:
        c.y-=speed
    elif keyboard.s:
            c.y +=speed
    elif keyboard.A:
       c.x-=speed
    elif keyboard.D:
        c.x+=speed
    if c.colliderect(cookie):
        score +=1
        cookie.pos=(randint(100,900),randint(100,500))
pgzurun.go()
