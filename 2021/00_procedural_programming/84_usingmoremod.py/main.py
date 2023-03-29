from math import sin, pi, radians
from random import randint
from datetime import datetime as dt

def sin_versi_saya(angle):
	return sin(radians(angle))

def lempar_dadu():
	return randint(1, 6)
"""
print(sin(pi/6))
print(sin_versi_saya(30))
"""

print(lempar_dadu())
print(dt.now())
print(dt.now(). year)