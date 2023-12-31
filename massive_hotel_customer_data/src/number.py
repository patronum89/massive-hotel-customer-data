import random

def randomnumber(n):
    minimum = pow(10 , n-1)
    maximum = pow(10 , n) - 1
    return random.randint(minimum , maximum)