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

def polygon(t, n, length):
    """Draws a n sides regular polygon with the given length.
    And t is a turtle.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)
polygon(bob, 5, 70)

lt(bob, (180-72)/2)
fd(bob, (70/2/math.cos((2*math.pi*54/360))))

for i in range(5):
    lt(bob, -180)
    fd(bob, (70/2/math.cos((2*math.pi*54/360))))
    lt(bob, 180-54)
    fd(bob, 70)
    lt(bob, 180-54)
    fd(bob, (70/2/math.cos((2*math.pi*54/360))))
pu(bob)
rt(bob, 54)
fd(bob, 200)
pd(bob)


wait_for_user()
