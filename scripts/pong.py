from enum import IntFlag
import turtle


print(type(turtle))

window = turtle.Screen()
window.title('Pong by V')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0.01)


class Sides(IntFlag):
    L = -1
    R = 1


class Paddle(object):

    def __init__(self, side=Sides.L, abs_max_x=350, abs_max_y=300, step_y=20, width=20):
        self.abs_max_y = abs_max_y
        self.step_y = step_y
        self.p = turtle.Turtle()
        self.p.shape('square')
        self.p.shapesize(stretch_len=1, stretch_wid=5)
        self.p.color('white')
        self.p.penup()
        self.p.goto((abs_max_x + width)*side, 0)

    def up(self):
        self.p.sety(self.p.ycor() + self.step_y if self.p.ycor() + self.step_y < self.abs_max_y else self.abs_max_y)

    def down(self):
        self.p.sety(self.p.ycor() - self.step_y if self.p.ycor() - self.step_y > - self.abs_max_y else -self.abs_max_y)


class Ball(object):
    def __init__(self, abs_max_x=350, abs_max_y=300):
        self.b = turtle.Turtle()
        self.b.shape('square')
        self.b.color('white')
        self.b.penup()
        self.b.goto(0, 0)
        self.v_x = 1
        self.v_y = 1
        self.dt = 1
        self.abs_max_x = abs_max_x
        self.abs_max_y = abs_max_y

    def animate(self):
        self.b.setx(self.b.xcor() + self.v_x*self.dt)
        self.b.sety(self.b.ycor() + self.v_y*self.dt)

    def collision(self):
        if (abs(self.b.ycor())) > self.abs_max_y:
            self.v_y *= - 1
        if (abs(self.b.xcor())) > self.abs_max_x:
            self.v_x *= - 1


ball = Ball()
paddle_left = Paddle(side=Sides.L)
paddle_right = Paddle(side=Sides.R)

while True:
    paddle_left.down()
    paddle_right.up()
    ball.animate()
    ball.collision()
    window.update()
