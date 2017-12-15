import turtle

def generate(n, result='F'):
    for _ in range(n):
        result = result.replace('F', 'F+F-F-F+F')
        print(result)
    return result

def draw(cmds, size=2):
    stack = []
    for cmd in cmds:
        if cmd == 'F':
            turtle.forward(size)
        elif cmd == '-':
            turtle.left(90)
        elif cmd == '+':
            turtle.right(90)
        elif cmd == '[':
             stack.append((turtle.position(), turtle.heading()))
        elif cmd == ']':
             position, heading = stack.pop()
             turtle.penup()
             turtle.setposition(position)
             turtle.setheading(heading)
             turtle.pendown()
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
    turtle.speed(1)
    #setup()
    turtle.left(180)
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 400, -turtle.window_height() + 400)
    turtle.pendown()
    koch = generate(7)
    draw(koch, 30)
    turtle.exitonclick()