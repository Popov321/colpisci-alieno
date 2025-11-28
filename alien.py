from pgzero.actor import Actor
from pgzero.clock import clock
from random import randint
import pgzrun

TITLE="Colpisci l'alieno"
WIDTH=1000
HEIGHT=1000

messaggio=""
alieno = Actor("alieno")
def draw():
    screen.clear()
    screen.fill(color=(128, 0, 0))
    alieno.draw()
    screen.draw.text(messaggio, center=(400,40), fontsize=60)
def piazza_alieno():
    alieno.x = randint(50, WIDTH-50)
    alieno.y = randint(50, HEIGHT-50)
    alieno.images = "alien"
def on_mouse_down(pos):
    global messaggio
    if alieno.collidepoint(pos):
        messaggio = "Bel Colpo!"
        alieno.images = "esplosione"
    else:
        messaggio = "Mancato..."
piazza_alieno()
clock.schedule_interval(piazza_alieno, 1.0)
pgzrun.go()