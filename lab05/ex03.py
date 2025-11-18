# Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. The class should provide methods to access elements (get and set methods) and some mathematical functions such as transpose, matrix multiplication and a method that allows iterating through all elements from a matrix an apply a transformation over them (via a lambda function).

class CoolMatrix:
  __init__(self, n, m):
    self.n = n
    self.m = m
    self.matrix = n * [m * [0, for ]]