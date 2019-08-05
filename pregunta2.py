import math
import numpy as np
import matplotlib.pyplot as plt 

def function(u,phi):            # funcion integrando

    denominador = math.cos(phi-(u**2))-math.cos(phi)
    return u/math.sqrt(denominador)

def simpson_1_3(phi,N):         # aproximacion simpson 1/3, N impar

    # valor del paso
    h = math.sqrt(phi)/N        

    # listas para guardar puntos y evaluacion
    x = []
    fx = []

    i = 0
    fx.append(0)
    while i <= N-1:
        x.append((i+1)*h)
        fx.append(function(x[i],phi))
        i += 1

    # calcular integral
    int = 0
    k = 0
    while k <= N:
        if k == 0 or i == N:
            int += fx[i]
        elif i % 2 != 0:
            int += 4*fx[i]
        else:
            int += 2*fx[i]
        k += 1
    return int*h/3

phi0 = math.pi/4

T_T0 = (2*math.sqrt(2)/math.pi)*simpson_1_3(phi0,100000)
T_T0

#function(0.1,phi0)

#a = math.cos(phi0)-math.cos(phi0-0.001**2)
#0.001/math.sqrt(a)
#a
#pkill -9 python