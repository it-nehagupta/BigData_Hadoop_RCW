#! / usr/bin/env/python3

import matplotlib.pyplot as draw

x=range(0,100)[::5]
y=range(100,200)[::5]

x1=range(0,30)[::3]
y1=range(40,70)[::3]


draw.plot(x,y,color='green')
draw.plot(x1,y1, color='blue')
draw.bar(x1,y1, color='red')
draw.bar(x,y,color='yellow')
draw.show()


