import turtle

def processString(oldStr):
    newstr=''
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    if ch == '1':
        newstr = '11'
    elif ch == '0' or 0:
        newstr = '1[0]0'
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

def draw(cmds, size = 2):
    stack = []
    for cmd in cmds:
        if cmd == '0' or 0:
            turtle.forward(size)
        if cmd == '1':
            turtle.forward(size)
        elif cmd == '[':
            stack.append((turtle.position(), turtle.heading()))
            turtle.left(45)
        elif cmd == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.pendown()
            turtle.right(45)
        else:
            print('Here is the Problem', cmd)
            raise ValueError("Unknown Cmd: {}".format(ord(cmd)))

        turtle.update()
if __name__ == '__main__':
    turtle.speed(1)
    # setup()
    turtle.left(180)
    turtle.penup()
    turtle.goto(-turtle.window_width() / 2 + 400, -turtle.window_height() + 400)
    turtle.pendown()
    bin = createLsystem(10, '0')
    draw(bin)
    turtle.exitonclick()