from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
susan = Turtle()
tom = Turtle()
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


def arc(t, r, angle):
    """Draws a arc with the given angle and radius."""
    arc_length = 2 * math.pi * r * angle/360.0
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle) 
arc(tom, 90, 135)

def circle(t, r):
    """Draws a circle with the given r radius."""
    arc(t, r, 360)
circle(susan, 80)

wait_for_user()
