import turtle 
import random 
import time 

colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"] 
turtle.shape('turtle') 
turtle.setup(550, 550) 
turtle.screensize(500, 500) 
turtle.pensize(5) 

turtleFile = open("C:/FirstPython/Chapter09/turtleTrace.txt", "w") 
for _ in range(30) : 
    x = random.randint(-250, 250) 
    y = random.randint(-250, 250) 
    color = random.choice(colorList) 
    turtle.pencolor(color) 
    turtle.goto(x,y) 
    outStr = str(x) + " " + str(y) + " " + color + " \n" 
    turtleFile.writelines(outStr) 
turtleFile.close( ) 
turtle.reset( ) 

time.sleep(5) 
turtle.pensize(5) 
turtleFile = open("C:/FirstPython/Chapter09/turtleTrace.txt", "r") 
while True : 
    inStr = turtleFile.readline( ) 
    if inStr == "" : 
        break 
    x, y, color = inStr.split( ) 
    turtle.pencolor(color) 
    turtle.goto(int(x),int(y)) 

turtleFile.close( ) 
turtle.done( ) 
