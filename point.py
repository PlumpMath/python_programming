# Representation - start
from operator import sub, mul
from math import sqrt
#Constructor
def make_point(x, y):
    return (x, y)

#Selector
def x_coordinate(point):
    return point[0]

#Selector
def y_coordinate(point):
    return point[1]

#Selector
def distance_between_points(p1, p2):
    return sqrt(square(sub(p1[0],p2[0])) + square(sub(p1[1],p2[1])))

#helper for selector
def square(a):
    return mul(a, a)

#Representation - end

#Use - start

def get_x_coordinate(point):
    return x_coordinate(point)

def get_y_coordinate(point):
    return y_coordinate(point)

#Use - end