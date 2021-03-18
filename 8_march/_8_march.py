from random import randint
from turtle import Turtle, Screen
import math
COLORS = ["green", "orange", "red", "yellow"]
class MyTurtle(Turtle):



    def petals(self, size=30, count=8, speed=100):
        if size == 30:
            self.begin_fill()



        if size > 0:  
            self.fd(3)
            self.rt(3)



            screen.ontimer(lambda: self.petals(size - 1, count, speed), speed)
            return



        if size == 0:
            self.rt(90)



        if size > -30:
            self.fd(3)
            self.rt(3)



            screen.ontimer(lambda: self.petals(size - 1, count, speed), speed)
            return



        self.end_fill()
        self.lt(230)



        if count > 0:
            screen.ontimer(lambda: self.petals(count=count - 1, speed=speed), speed)
            return



        self.hideturtle()



    def stem(self):
        self.pencolor('green')
        self.fd(250)



    def flowerhead(self):
        self.pencolor('red')



        self.petals(speed=randint(50, 250))



def flower2():
    tony.color('green', 'purple')
    tony.penup()
    tony.goto(0, -200)
    tony.pendown()
    tony.showturtle()
    tony.goto(80, -15)
    tony.rt(40)
    tony.flowerhead()



def flower3():
    tina.color('green', 'turquoise')
    tina.penup()
    tina.goto(0, -200)
    tina.pendown()
    tina.showturtle()
    tina.goto(-80, -15)
    tina.lt(40)
    tina.flowerhead()



def flower5():
    tweeny.color('green', 'pink')
    tweeny.penup()
    tweeny.goto(0, -200)
    tweeny.pendown()
    tweeny.showturtle()
    tweeny.goto(-160, -25)
    tweeny.lt(40)
    tweeny.flowerhead()



def draw_polygons(point, size):
    area = 20000
    twixy = Turtle()
    twixy.speed('fastest')
    twixy.penup()
    twixy.sety(point)
    side_length = math.sqrt(area * math.atan(math.pi / size))

    for a_color in COLORS:
        print("aaa", a_color)

        for _ in range(12):

            twixy.fillcolor(a_color)

            twixy.forward(3 * side_length / 10)
            twixy.right(15)

            twixy.left(112)
            twixy.pendown()
            twixy.begin_fill()

            for _ in range(2):
                twixy.forward(side_length * 2)
                twixy.left(90)
                twixy.forward(side_length / 2)
                twixy.left(90)
            twixy.end_fill()
            twixy.penup()
            twixy.right(112)

            twixy.forward(3 * side_length / 10)
            twixy.right(15)

        twixy.forward(2 * side_length / 13)
        twixy.right(7.5)

def draw_circle():
    draw_polygons(300, 50)

def draw_circle1():
    draw_polygons(75, 30)

screen = Screen()
tony = MyTurtle(shape='turtle', visible=False)
tina = MyTurtle(shape='turtle', visible=False)
tweeny = MyTurtle(shape='turtle', visible=False)

screen.ontimer(flower2, 110)
screen.ontimer(flower3, 110)
screen.ontimer(flower5, 110)
screen.ontimer(draw_circle, 110)
screen.ontimer(draw_circle1, 110)


screen.mainloop()
