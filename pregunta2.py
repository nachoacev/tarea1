import math
import numpy as np
import matplotlib.pyplot as plt 

def function(u,phi):            # funcion integrando
    denominador = math.sqrt(math.cos(phi)-math.cos(phi-(u**2)))
    return u/denominador

def simpson_1_3(phi,N):         # aproximacion simpson 1/3, N par

    # valor del paso
    h = math.sqrt(phi)/N        

    # listas para guardar puntos y evaluacion
    x = []
    fx = []

    while i <= N:
        x.append(i*h)
        fx.append(function(x[i]))
        i += 1

    # calcular integral
    int = 0
    k = 0
    while k <= N:
        if k == 0 or i == N:
            int += fx[i]
        elif i % 2 != 0:
            int += 4*fx[i]
