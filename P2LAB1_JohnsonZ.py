# ZNiyah Johnson
# 2/18/25
# P2Lab1 Using math expressions and formatting float values
# import math module to use the constant, math.pi

import math

radius = float(input("What is the radius of a circle? "))

diameter = radius*2

circumference = 2* radius * math.pi

area = math.pi * math.pow(radius,2)


print(f'The diameter of a circle is {diameter:.1f}\n')
print(f'The circumference of a circle is {circumference:.2f}\n')
print(f'The area of a circle is {area:.3f}\n')







