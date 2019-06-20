#! /usr/bin/env/python3

import matplotlib.pyplot as b_g

x=[2,4,7]
y=[1,3,5]
x1=[1,4,6]
y1=[3,2,5]
b_g.title("comparison between two objects")
b_g.bar(x,y,color='red', label="bar chart of data")
b_g.bar(x1,y1,color='green', label="bar chart of another data")

#legend is used to show the label

b_g.legend()
b_g.show()
