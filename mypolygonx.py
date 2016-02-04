from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1

def triangle(t, n, length):
    d = float(length)/2
    a = (180.0 - 360.0/n)/2
    l = d/math.cos(2*math.pi*a/360.0)
    fd(t, l)
    lt(t, 180.0-a)
    fd(t, length)
    lt(t, 180.0-a)
    fd(t, l)
    lt(t, -180)

def umbrella(t, n, length):
    for i in range(n):
        triangle(t, n, length)

n = 5
for i in range(3):
    umbrella(bob, n, 120)
    n += 1
    pu(bob)
    fd(bob, 300)
    pd(bob)

wait_for_user()
