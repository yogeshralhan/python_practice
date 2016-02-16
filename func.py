
#case using this import method
"""
from math import pi

def circle(radius):
	return pi*(radius**2)

while True:
	ra=input("enter radius")
	print circle(ra)
"""

#case using this import method

import math

def cir(rad):
	return math.pi*(abs(rad**2))

while True:
	r=input("enter the radius")
	print cir(r)
