from random import *
from turtle import *

screen = Screen()
screen.setup(475, 480, 365, 0)
screen._root.resizable(False, False)

gif_List = ["MemoryGame\MemGifs\cat[0].gif", "MemoryGame\MemGifs\cat[1].gif", "MemoryGame\MemGifs\cat[2].gif"
            "MemoryGame\MemGifs\EyesOnTheTable.gif"]
GIF = choice(gif_List)
tiles = list(range(50)) * 2
state = {'mark': None}
hide = [True] * 100



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 250) // 50 + ((y + 250) // 50) * 10)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 10) * 50 - 250, (count // 10) * 50 - 250


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(GIF)
    stamp()

    for count in range(100):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(500, 500, 370, 0)
addshape(GIF)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
