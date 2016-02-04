from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        rt(t, angle)

def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360.0
    n = int(arc_length/3)+1
    step_length = float(arc_length/n)
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)

def draw_a(t, length, angle):
    rt(t, float(angle)/2+90)
    fd(t, length)
    pu(t)
    rt(t, 180)
    fd(t, length)
    rt(t,180.0-float(angle))
    pd(t)
    fd(t, length)
    pu(t)
    lt(t, 180.0)
    fd(t, length)
    lt(t, 180.0-float(angle))
    fd(t, 2*length/3)
    lt(t, 90+float(angle)/2)
    pd(t)
    fd(t, 2*(2*length/3*math.cos(math.pi/2-2*math.pi*angle/2/360.0)))
    pu(t)
    fd(t, 200)

draw_a(bob, 70, 50)

def draw_b(t, length):
    pd(t)
    rt(t)
    fd(t, float(length))
    lt(t)
    fd(t, float(length*0.3))
    lt(t)
    pu(t)
    fd(t, float(length/2))
    lt(t)
    pd(t)
    fd(t, float(length*0.3))
    pu(t)
    rt(t)
    fd(t, float(length/2))
    rt(t)
    pd(t)
    fd(t, float(length/4))
    for i in range(2):
        arc(t, float(length)/4, 184.0)
#       pu(t)
#       lt(t)
#       fd(t, 1)
#       lt(t)
#       pd(t)
        lt(t, 180)
        fd(t, length*0.04)
    pu(t)
    lt(t, 180)
    fd(t, 200)

draw_b(bob, 170)

wait_for_user()
