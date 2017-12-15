import turtle

def generate(n, result='A'):
    for _ in range(n):
        result = result.replace('A','ABA')
        result = result.replace('B', 'BBB')
    print(result)
    return result
def draw(cmds, size=2):
    stack=[]
    for cmd in cmds:
        if cmd == 'A':
            turtle.forward(size)
        elif cmd == 'B':
            turtle.penup()
            turtle.setx(turtle.xcor()+ size)
            turtle.pendown()

        else:
            raise ValueError("Unknown Cmd: {}".format(ord(cmd)))
        turtle.update()

if __name__ == '__main__':
    turtle.speed(0)
    # setup()
    turtle.left(180)
    turtle.penup()
    turtle.goto(0, turtle.window_height()/2)
    turtle.pendown()
    cant = generate(10)
    draw(cant, 10)
    turtle.exitonclick()