import math

def squareroots(a):
    prompt = raw_input('Enter a estimated value: ')
    x = float(prompt)
    accuracy = raw_input('Enter the degree of accuracy (e.g. 0.0000001): ')
    epsilon = float(accuracy)
    while True:
        print x
        y = (x+a/x)/2
        if abs(y-x) < epsilon:
            break
        x = y
