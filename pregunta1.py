import numpy as np
import math
import matplotlib.pyplot as plt

t = 1.258  # punto a estimar
h = np.logspace(-1,-15,15,base=10.0)

diff_simple = []
diff_mejor = []

def f_util(x):                     # funcion a estudiar
    return math.sin(x/2)

valor_exacto = math.cos(1.258/2)/2 # valor mas cerca al teorico

for i in range(15):                # lista con diff de derivada teori y aproxim
    df1 = (-f_util(t+2*h[i])+8*f_util(t+h[i])-8*f_util(t-h[i])+f_util(t-2*h[i]))/(12*h[i])
    df2 = (f_util(t+h[i])-f_util(t))/h[i]
    diff_mejor.append(abs(df1-valor_exacto))
    diff_simple.append(abs(df2-valor_exacto))

# ploteo
plt.plot(h, diff_mejor, color='g', label="Derivada simetrica")
plt.plot(h, diff_simple, color='b', label="Derivada simple")
plt.xscale('log')
plt.yscale('log')
#plt.ylim(1e-12, 1e-1)
#plt.axhline(0)
plt.xlabel('h', fontsize=20)
plt.ylabel('$\\frac{d}{dx}sin(x/2) - \\frac{1}{2}cos(x/2)$', fontsize=20)
plt.legend(loc='lower left')
#_ = plt.xticks(h[::2])