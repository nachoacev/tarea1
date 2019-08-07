import numpy as np
import math
import matplotlib.pyplot as plt

h = np.logspace(-1,-15,15,base=10.0)         # diferentes h's float64
H = np.float32(np.logspace(-1,-15,15,base=10.0)) # diferentes h's float32

diff_simple_mejor64 = [[],[]]
#diff_mejor64 = []

diff_simple_mejor32 = [[],[]]
#diff_mejor32 = []

t = 1.258
valor_exacto = math.cos(1.258/2)/2
T = np.float32(np.asarray([t]))


def f_util(x):
    return math.sin(x/2)

def aprox1_4(t,h):                         #aproximacion orden 1 y 4
    return [(f_util(t+h)-f_util(t))/h, (-f_util(t+2*h)+8*f_util(t+h)-8*f_util(t-h)+f_util(t-2*h))/(12*h)]

#def aprox4(t,h):                         #aproximacion orden 4
 #   return (-f_util(t+2*h)+8*f_util(t+h)-8*f_util(t-h)+f_util(t-2*h))/(12*h)

for i in range(len(h)):                   #añadir diff a listas
    df_64 = aprox1_4(t,h[i])              #diff con floats 64
    df_32 = aprox1_4(T[0],H[i])             #diff con floats 32
    
    #agregar

    diff_simple_mejor32[0].append(np.abs(df_32[0]-valor_exacto))
    diff_simple_mejor32[1].append(np.abs(df_32[1]-valor_exacto))
    diff_simple_mejor64[0].append(np.abs(df_64[0]-valor_exacto))
    diff_simple_mejor64[1].append(np.abs(df_64[1]-valor_exacto))

plt.plot(h, diff_simple_mejor64[1], color='g', label="Derivada simetrica")
plt.plot(h, diff_simple_mejor64[0], color='b', label="Derivada simple")
plt.yscale('log')
plt.xscale('log')
#plt.ylim(1e-12, 1e-1)
plt.axhline(0)
plt.xlabel('h', fontsize=20)
plt.ylabel('$\\frac{d}{dx}sin(x/2) - \\frac{1}{2}cos(x/2)$', fontsize=20)
plt.legend(loc='lower left')
plt.title('float64')
#_ = plt.xticks(h[::2])

plt.plot(h, diff_simple_mejor32[1], color='g', label="Derivada simetrica")
plt.plot(h, diff_simple_mejor32[0], color='b', label="Derivada simple")
plt.yscale('log')
plt.xscale('log')
#plt.ylim(1e-12, 1e-1)
plt.axhline(0)
plt.xlabel('h', fontsize=20)
plt.ylabel('$\\frac{d}{dx}sin(x/2) - \\frac{1}{2}cos(x/2)$', fontsize=20)
plt.legend(loc='lower left')
plt.title('float32')