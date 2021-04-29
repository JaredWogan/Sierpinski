import turtle
from tkinter import *
import time
import os

dir = os.getcwd()

def drawTriangle(points,color,myTurtle):
    myTurtle.pencolor('black')
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    #colormap = ['#6E00FF','#0074FF']
    colormap=['white','#00FF9C']
    drawTriangle(points,colormap[degree%2],myTurtle)
    midPoints=[getMid(points[0], points[1]), getMid(points[0], points[2]), getMid(points[1],points[2])]
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
    if degree%2==0: drawTriangle(midPoints,colormap[degree%2-1],myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   #turtle.screensize(1920,1080)
   myTurtle.speed(1)
   turtle.bgcolor('#00FF9C')
   size = 300
   Points = [[-size,-size/2-100],[0,size-100],[size,-size/2-100]]
   sierpinski(Points,5,myTurtle)
   myTurtle.getscreen().getcanvas().postscript(file=dir+'/Sierpinski/Alicias-Sierpinski.eps')
   myWin.exitonclick()

if __name__ == '__main__':
    main()
