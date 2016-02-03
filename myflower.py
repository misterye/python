from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and 
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)
        print "Segment ",i+1
        print "Angle is %d now", (i + 1) * float(angle)

def arc(t, r, angle):
    """Draws a arc with the given angle and radius."""
    arc_length = 2 * math.pi * r * angle/360.0
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle) 

for i in range(7):
    for j in range(2):
        arc(bob, 60, 60)
        lt(bob, 180-60)
    lt(bob, 360.0/7)
pu(bob)
fd(bob, 200)

pd(bob)
for i in range(10):
    for j in range(2):
        arc(bob, 40, 80)
        lt(bob, 180-80)
    lt(bob, 360.0/10)
pu(bob)
fd(bob, 200)

pd(bob)
for i in range(20):
    for j in range(2):
        arc(bob, 140, 20)
        lt(bob, 180-20)
    lt(bob, 360.0/20)
pu(bob)

wait_for_user()
