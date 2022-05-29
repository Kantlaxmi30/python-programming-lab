##Write a Python program to convert degree to radian.

from math import pi
def degrees_to_rads(deg):
  return (deg * pi) / 180.0
print(degrees_to_rads(180))
print(degrees_to_rads(90))