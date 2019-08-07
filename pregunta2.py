import math
import numpy as np
import matplotlib.pyplot as plt 

# Determinacion de algoritmo simpson para el integrando

def function(u,phi):            # funcion integrando

    denominador = math.cos(phi-(u**2))-math.cos(phi)
    return u/math.sqrt(denominador)

def trapecio(phi,N):            # aproximacion por trapecio, N entero

    # valor del paso
    h = math.sqrt(phi)/N

    k = 1                         # no evaluamos el integrando en 0 porque se infedine
    suma = 0                       # valor suma
    while k <= N:
        if k == N:                # no evaluamos el principio
            suma += function(k*h,phi)
        else:
            suma += 2*function(k*h,phi)
        k += 1
    return suma*h/2

trapecio(math.pi/4,100)

# uso de simpson para distintos phi's y N's de manera recursiva
# simpson(2N) = (4*trapecio(2N)-trapecio(N))/3

phi = np.flip(np.linspace(math.pi/2,0,1000,endpoint=False))

integrales = []             # guarda las integrales para distintos phi's

#for i in range(1,len(phi)):
#    N = 20
#    simpson_2N = 0
 #   simpson_4N = 1
  #  error = 1
   # while error > 0.01:
    #    simpson_4N =  (4*trapecio(phi[i],2*N+2)-trapecio(phi[i],N+1))/3
     #   error = math.fabs(simpson_2N-simpson_4N)/simpson_4N)
      #  if error <= 0.01:
       #     integrales.append(simpson_4N)
        #else:
         #   simpson_2N = simpson_4N
          #  N = 2*N
   # i += 1     

for i in range(1,len(phi)):
    N = 10
    trap_N = 0
    trap_2N = 0
    trap_4N = 1
    error = 1
    p = phi[i]
    while error > 0.01:
        trap_N = trapecio(p,N)
        trap_2N = trapecio(p,2*N)
        trap_4N = trapecio(p, 4*N)
        error = math.fabs((4*trap_4N-5*trap_2N+trap_N)/(4*trap_2N-trap_N))
        N = 2*N
    integrales.append((4*trap_4N-trap_2N)/3)