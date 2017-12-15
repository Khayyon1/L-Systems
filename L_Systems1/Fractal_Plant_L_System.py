import sys
import turtle

def generate(n, result = '[X]'):
    '''
    :param n used for arbritary iteration of string entered
    :param result is set to the beginning axiom for the fractal plant
    :return The results based on the rules of the L-System in use
    '''
    for _ in range(n):
        # Rule #1
        result = result.replace('X', 'F[-X][X]F[-X]+FX')

        #Rule #2
        result = result.replace('F', 'FF')
    print(result)
    return result

def draw(cmds, size=2):
    stack = []
    for cmd in cmds:
        if cmd == 'F':
            turtle.forward(size)
        elif cmd == '-':
            turtle.left(25)
        elif cmd == '+':
            turtle.right(25)
        elif cmd == 'X':
            pass
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
    turtle.goto(0, -turtle.window_height()/2)

if __name__ == '__main__':
    setup()
    plant = generate(7)
    draw(plant, 3)
    turtle.exitonclick()