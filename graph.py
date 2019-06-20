#! /usr/bin/python3

import matplotlib.pyplot as draw

x=[5,4]
y=[2,8]
p=[1,6]
q=[3,7]

draw.xlabel("Time")
draw.ylabel("Distance")
draw.title("Analysis of distance and time")
draw.plot(x,y, color='green',label="Science data")
draw.legend()
draw.scatter(p,q, s=100, c='r')
draw.show()


