import sympy as sym

sym.init_printing()
x,y,z = sym.symbols('x,y,z') # simbolos
c1 = sym.Symbol('c1') # simbolos
f = sym.Eq( 2*x**2 + y + z ,  1)
g = sym.Eq( x + 2*y + z    , c1)
h = sym.Eq(-2*x + y        , -z)

# Dos soluciones: x,y,z
print(sym.solve([f,g,h],(x,y,z)))


