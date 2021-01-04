import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.randn(4, 100)
data2 = np.random.randn(4, 100)
#plt.plot(data1, data2,marker=11) # caretdown marker (centered at base)
plt.plot(data1, data2,marker='+') # plus sign
plt.show()
# my_plotter(ax, data1, data2, {'marker': 'x'})


"""
# ejercicio 2  y = sen(x), 100 elementos para x desde 0 hasta 20
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
print(x)
plt.plot(x, np.sin(x))
plt.show()
"""