# --------------
import pandas as pd
import numpy as np
import math


#Code starts here

class complex_numbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return complex_numbers(r,i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return complex_numbers(r,i)        
    
    def __mul__(self, other):
        r = self.real*other.real - self.imag*other.imag
        i = self.imag*other.real + self.real*other.imag
        return complex_numbers(r,i)
    
    def __truediv__(self, other):
        r = (self.real*other.real + self.imag*other.imag)/(other.real**2 + other.imag**2)
        i = (self.imag*other.real - self.real*other.imag)/(other.real**2 + other.imag**2)
        return complex_numbers(r,i)

    def absolute(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def argument(self):
        return math.degrees(math.atan(self.imag/self.real))

    def conjugate(self):
        return complex_numbers(self.real, -self.imag)

comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)

comp_sum = comp_1 + comp_2
print(comp_sum)
comp_diff = comp_1 - comp_2
print(comp_diff)
comp_prod = comp_1 * comp_2
print(comp_prod)
comp_quot = comp_1 / comp_2
print(comp_quot)
comp_abs = comp_1.absolute()
print(comp_abs)
comp_conj = comp_1.conjugate()
print(comp_conj)
comp_arg = comp_1.argument()
print(comp_arg)






