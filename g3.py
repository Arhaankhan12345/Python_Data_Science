from math import gamma
from re import A
import pgzrun



WIDTH = 1000
HEIGHT = 500

P = Actor('chick',(100,100))
e = Actor("walrus",(500,200))

p.speed = 3
e.speed = 2
gameover = False
def player_movement():
    if keyboard.w:
        p.y -= p.speed
    if keyboard.s:
        p.y += p.speed
    if keyboard.A:
        p.x -= p.speed
    if keyborad.D:
        p.x += p.speed
        #boundary handling
    if p.x< 0: #agar player left sife se bahar ja raha h
        p.x = WIDTH #TO RIGHT SIDE PE DIKHNE LAGE
    if p.x > WIDTH: #VICE VERSA
        p.X < 0
    if p.y <0:
        p.y = HEIGHT

def enemy_movement():
    if p.y > e.y:
        e.y += e.speed
    if p.y <= e.y:
        e.y -= e.speed
    if p.x >e.x:
        e.x += e.speed
        if p.x <= e.x:
         e.x -= e.speed

def check_collision():
    global gameover
    if e. coolliderect(p):
        p.image = 'cookie'
        gameover = True

def draw():
    if not gameover:
        screen.clear()
        e.draw()
        P.draw()

    else:
        screen.fill("crimson")
        screen.draw.text("Game over",center=(WIDTH//2,HEIGHT//2),COLOR="WHIT",fontsize=100)
    def update():
        player_movement()
        enemy_movement()
        check_collision()

    pgzrun.go






            

