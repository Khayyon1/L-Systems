import sys
import turtle

def processString(oldStr):
    newstr=''
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'X+YF+'
    elif ch == 'Y':
        newstr = '-FX-Y'
    else:
        newstr = ch
    return newstr

def createLsystem(num, axiom):
    start=axiom
    end = ""
    for i in range(num):
        end = processString(start)
        start = end
    return end

def draw(cmds, size=2):
    for cmd in cmds:
        if cmd == 'F':
            turtle.forward(size)
        elif cmd == '-':
            turtle.left(90)
        elif cmd == '+':
            turtle.right(90)
        elif cmd == 'X':
            pass
        elif cmd == 'Y':
            pass
        else:
            raise ValueError("Unknown Cmd: {}".format(ord(cmd)))
        turtle.update()

def setup():
    turtle.hideturtle()
    turtle.tracer(1e3, 0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -turtle.window_height()/2 + 250)

if __name__ == '__main__':
    turtle.speed(0)
    # #setup()
    # turtle.left(180)
    # turtle.penup()
    # turtle.goto(-turtle.window_width() / 2 + 400, -turtle.window_height() + 400)
    # turtle.pendown()
    dragon = createLsystem(10, 'FX')
    draw(dragon, 15)
    #turtle.exitonclick()