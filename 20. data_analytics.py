# 1. Find the odd and even elements in an array.
import numpy as np
xyz =  np.array([1,2,3,4,5,6,7,8,9])
oddele = xyz[xyz % 2!= 0]
eveele = xyz[xyz %  2 == 0]
print("Odd elements:", oddele)
print("Even elements:", eveele)
