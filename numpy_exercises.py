import numpy as np 

""" 
(1) Sistema de Ecuaciones
2 * x + 3 * y = 10
3 * x –     y = -1.5
"""

M = np.array([[2,3],[3,-1]])
V = np.array([10,-1.5])
print("Eq1 ")
print(np.linalg.solve(M,V) )   # algebra lineal

""" 3x - 9y = -42
    2x + 4y = 2
"""

A = np.array([ [3,-9], [2,4] ])
b = np.array([-42,2])
print("Eq2 ")
print(np.linalg.solve(A,b))

""" 
 x - 2y - z  = 6
2x + 2y - z  = 1
-x -  y + 2z = 1

"""
M = np.array([ [1,-2,-1], [2,2,-1], [-1,-1,2] ])
c = np.array([6,1,1])
print("Eq3 ")
print(np.linalg.solve(M,c))
