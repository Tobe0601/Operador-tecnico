def add(a, b):
    return a + b

print(add(2, 3))

def hours_to_minutes (hours):
    return hours * 60

print(hours_to_minutes(5))

def is_between(x, low, high):
    return low <= x <= high

print(is_between(5, 1, 10))
print(is_between(15, 1, 10))


import math

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(3))