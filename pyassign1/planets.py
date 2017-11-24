"""planets.py: a simulator of six main planets in solar system

__author__="GuoXiao"
__pkuid__="1700011795"
__email__="pkuguoxiao@pku.edu.cn"
"""


import turtle
import math

def main():
    wn = turtle.Screen()
    turtlelist=["sun","murcury","venus","earth","mars","jupiter","saturn"]
    colorlist=["Yellow","Blue","Gold","Green","Red","Black","Orange"]
    distancelist=[0,38,72,100,150,200,260]
    alist=[0,38,72,100,150,200,260]
    blist=[0,20,50,80,120,150,180]
    pi=math.pi
    speedlist=[0,1,2,3,4,5,6]
    for i in range(7):
        turtlelist[i]= turtle.Turtle()
        turtlelist[i].speed(speedlist[i])
        turtlelist[i].color(colorlist[i])
        turtlelist[i].shape("circle")
        turtlelist[i].pensize(5)
        turtlelist[i].up()
        turtlelist[i].goto(distancelist[i],0)
    for i in range(0,360,1):
        for j in range(7):
            turtlelist[j].pendown()
            x=alist[j]*math.cos(i/180*math.pi)
            y=blist[j]*math.sin(i/180*math.pi)
            turtlelist[j].goto(x,y)


if __name__=="__main__":
    main()
