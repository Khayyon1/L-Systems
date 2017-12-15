import turtle

def processString(oldStr):
    newstr=''
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-G+F+G-F'
    elif ch == 'G':
        newstr = 'GG'
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
        if cmd == 'F' or cmd == 'G':
            turtle.forward(size)
        elif cmd == '+':
            turtle.left(120)
        elif cmd == '-':
            turtle.right(120)
        else:
            raise ValueError("Unknown Cmd: {}".format(ord(cmd)))
        turtle.update()

if __name__ == '__main__':
    turtle.speed(0)
    #setup()
    turtle.left(180)
    # turtle.penup()
    turtle.goto(0, -turtle.window_height()/2 + 400)
    # turtle.pendown()
    sier = createLsystem(6, "F-G-G")
    draw(sier, 5)
    turtle.exitonclick()