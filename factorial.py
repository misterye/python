def factorial(n):
    if not isinstance(n, int):
        print "Factorial is only defined for integers."
        return none
    elif n < 0:
        print "Factorial is not defined for negative integers."
        return none
    elif n==0:
        return 1
    else:
        result = n * factorial(n-1)
        return result
