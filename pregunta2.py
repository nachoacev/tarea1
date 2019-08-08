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

    k = 1                       # no evaluamos el integrando en 0 porque se infedine
    suma = 0                    # valor suma
    while k <= N:
        if k == N:              # no evaluamos el principio
            suma += function(k*h,phi)
        else:
            suma += 2*function(k*h,phi)
        k += 1
    return suma*h/2

trapecio(math.pi/4,100)

# uso de simpson para distintos phi's y N's de manera recursiva
# simpson(2N) = (4*trapecio(2N)-trapecio(N))/3

phi = np.flip(np.linspace(math.pi/2,0,1000,endpoint=False))   # grilla de phi's, sin el 0

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

# iteracion de integrales

for i in range(len(phi)):
    N = 100
    p = phi[i]
    trap_N = trapecio(p,N)
    trap_2N = trapecio(p,2*N)
    trap_4N = trapecio(p, 4*N)
    error = 1
    while error > 0.01:
        error = math.fabs((4*trap_4N-5*trap_2N+trap_N)/(4*trap_2N-trap_N))
        N = 2*N
        trap_N = trap_2N
        trap_2N = trap_4N
        trap_4N = trapecio(p, 4*N)
    integrales.append((4*trap_4N-trap_2N)/3)

I = np.asanyarray(integrales)
T_To = (2*math.sqrt(2)/math.pi)*I

from scipy import integrate

T_To[500]

#sp.integrate.trapz()

#################################################

def trap_scipy(phi,N):
    i = 1                   # indice cambiante, no toma el punto inicial
    fx = []
    h = math.sqrt(phi)/N
    while i <= N:
        fx.append(function(i*h,phi))
        i += 1
    return integrate.trapz(fx,dx=h)

integrales2 = [[],[]]

for i in range(len(phi)):
    N = 200
    p = phi[i]
    h = math.sqrt(p)/N
    y = lambda u: function(u,p)
    integrales2[0].append(trap_scipy(p,N))
    integrales2[1].append(integrate.quad(y,h,math.sqrt(p))[0]) 

integrales2[1]

A = np.asanyarray(integrales2[0])
B = np.asanyarray(integrales2[1])

diff1 = (2*math.sqrt(2)/math.pi)*np.abs(A-I)
diff2 = (2*math.sqrt(2)/math.pi)*np.abs(B-I)

plt.plot(phi, diff1, color='g', label="diff trapecio")
plt.plot(phi, diff2, color='b', label="diff quad")
plt.legend(loc='lower left')