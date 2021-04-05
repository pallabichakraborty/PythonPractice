import turtle
import sys

wn = turtle.Screen()

sys.setExecutionLimit(200000)

turtleName = ['Liam','Noah','Oliver','William','Elijah','James','Benjamin','Lucas','Mason','Ethan','Olivia','Emma','Ava','Sophia','Isabella','Charlotte','Amelia','Mia','Harper','Evelyn']
turtleGroup=[]
colordata=['red','blue','green','orange','yellow','brown','pink','gray','turquoise','violet']

distance = 50
angle=10

for i in range(len(turtleName)):
    turtleGroup.append(turtle.Turtle())
    turtleGroup[i].name=turtleName[i]
    turtleGroup[i].pensize(i%10)
    # Add color to the arrows
    turtleGroup[i].pencolor(colordata[i%10])
    turtleGroup[i].right(angle)
    turtleGroup[i].forward(distance)
    turtleGroup[i].write(turtleGroup[i].name)
    angle=angle+18
    distance=distance+10
    
  
