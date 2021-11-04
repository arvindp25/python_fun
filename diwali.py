
 
from time import sleep
import turtle    # importing the module
trtl = turtle.Turtle()    #making a turtle object of Turtle class for drawing
screen=turtle.Screen()    #making a canvas for drawing
screen.setup(800,600)    #choosing the screen size
screen.bgcolor('black')    #making canvas black
# trtl.pencolor('brown')    #making colour of the pen red
# trtl.pensize(5)    #choosing the size of pen nib
trtl.speed(10)    #choosing the speed of drawing

def draw_dia(dia_start = -120, air_direction = "left" ):
    batti_angle = -90 if air_direction == "left" else 90
    trtl.setpos(dia_start,0)
    trtl.color("brown")
    trtl.begin_fill()
    trtl.right(100)
    trtl.circle(100,200)
    trtl.end_fill()
    
    trtl.setpos(dia_start+90,0)
    trtl.right(100)
    trtl.color('yellow')
    trtl.begin_fill()
    for i in range(2):
        trtl.circle(50,batti_angle)
        trtl.circle(50//2,batti_angle)
    trtl.end_fill()
    trtl.color('brown')

#     information printing


draw_dia(-400, air_direction = "left")
draw_dia(-200, air_direction = "right")
draw_dia(0, air_direction = "left")
draw_dia(200, air_direction = "right")

trtl.penup()
trtl.setpos(-150,120)
trtl.pendown()
trtl.pencolor('Red')
trtl.write('Happy Diwali', font=("Arial", 32, "bold"))
trtl.penup()
trtl.ht()
sleep(30)
