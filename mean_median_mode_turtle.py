"""import numpy 
import statistics

speed=[99,86,87,88,111,86,103,87,94,78,77,85,86]

speed.sort();  
print(speed)
print(numpy.median(speed))
print(numpy.mean(speed))
print(statistics.mode(speed))
"""
import turtle
t=turtle.Turtle()
t.color('black')
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)

t.left(180)
    
   



"""t.circle(50)
t.left(180)
t.forward(100)
t.left(180)

t.circle(50)"""

t.penup()
t.forward(300)
t.right(90)
t.forward(50)
t.pendown()

t.right(90)
t.forward(60)
t.right(60)
t.forward(70)
t.left(120)
t.forward(190)
t.right(60)
t.forward(100)
turtle.done()
