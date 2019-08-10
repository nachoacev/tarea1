"""
Se implementa, resuelve y compara la obtencion del periodo
T de un pendulo fisico en el caso de grandes amplitudes
Se usa el metodo de simpson 1/3 a travez del metodo del
trapecio.
Se compara dicho metodo con metodos propios del paquete
scipy, y se comparan los tiempos de ejecucion.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def func_int(x,phi):
    """funcion integrando sin cambio de variable
    """
    denominador = np.cos(x)-np.cos(phi)
    return 1/np.sqrt(2*denominador)

#ploteo del integrando (evitando el cero) con phi=pi/4
x_to_plot = np.flip(np.linspace(np.pi/4,0,1000,endpoint=False))

plt.clf()
plt.plot(x_to_plot, func_int(x_to_plot,np.pi/4),label='funcion integrando')
plt.title('funcion integrando sin cambio de variable')
plt.xlabel('$\\phi$', fontsize=20)
plt.ylabel('$f$', fontsize=20)
plt.legend()
plt.show()

def func_int_cv(u,phi):
    """funcion integrando dado el cambio de variable
    u = (phi-phi_o)**(1/2)
    """
    denominador = np.cos(phi-(u**2))-np.cos(phi)
    return u/np.sqrt(denominador)

#ploteo del integrando con el cv
u_to_plot = np.flip(np.linspace(np.sqrt(np.pi/4),0,1000,endpoint=False))

plt.clf()
plt.plot(u_to_plot, func_int_cv(x_to_plot,np.pi/4),label='funcion integrando')
plt.title('funcion integrando con cambio de variable')
plt.xlabel('u', fontsize=20)
plt.ylabel('$\\frac{f}{g\'}$', fontsize=20)
plt.legend()
plt.show()

#########################################################
# Obtencion de valores de T/To

def trapecio(func,a,b,N):       # aproximacion por trapecio, N entero
    # valor del paso
    h = (b-a)/N

    k = 1                       # no evaluamos el integrando en 0 porque se infedine
    suma = 0                    # valor suma
    while k <= N:
        if k == N:              # no evaluamos el principio
            suma += func(k*h,b)
        else:
            suma += 2*func(k*h,b)
        k += 1
    return suma*h/2

def simp_trap(func,a,b,tol = 0.0001):
    """Integra func de "a" a "b" con metodo simpson, 
    pero usando metodo trapecio S_(2N) = (4*T_(2N)-T_(N))/3
    """
    N = 10
    trap_N = trapecio(func,a,b,N)
    trap_2N = trapecio(func,a,b,2*N)
    trap_4N = trapecio(func,a,b,4*N)
    counter = 0
    error = 1
    while error > tol:
        error = np.fabs((4*trap_4N-5*trap_2N+trap_N)/(4*trap_2N-trap_N))
        N = 2*N
        trap_N = trap_2N
        trap_2N = trap_4N
        trap_4N = trapecio(func,a,b, 4*N)
        counter += 1
    return (4*trap_4N-trap_2N)/3, counter

phi_o = np.flip(np.linspace(np.pi/2,0,100,endpoint=False))
I = []
for i in range(len(phi_o)):
    I.append(simp_trap(func_int_cv,0,phi_o[i])[0])

T_To = 2*np.sqrt(2)*np.asarray(I)/np.pi



#ploteo del cuociente T/To

plt.clf()
plt.plot(phi_o,T_To,label='$\\frac{T}{T_o}(\\phi_o)$')
plt.plot(phi_o,phi_o, color='g')
plt.title('Periodo para distintos angulos de inicio ')
plt.xlabel('$\\phi _0$')
plt.ylabel('$\\frac{T}{T_0}$')


#######################################################
# Comparacion

quad = []
trap = []

def trap_scipy(func,a,b,tol = 0.0001):                 
    N = 10
    error = 1
    T1 = 0
    T2 = 1
    while error > tol:
        fx = []
        i = 1
        while i <= N:
            h = (b-a)/N
            fx.append(func(i*h,b))
            i += 1
        N = 2*N
        T1 = T2
        T2 = integrate.trapz(fx,dx=h)
        error = np.fabs((T2-T1)/T1)
    return T2


for i in range(len(phi_o)):
    quad.append(integrate.quad(func_int_cv,0,phi_o[i],phi_o[i])[0])
    trap.append(trap_scipy(func_int_cv,0,phi_o[i]))

Q = 2*np.sqrt(2)*np.asarray(quad)/np.pi
T = 2*np.sqrt(2)*np.asarray(trap)/np.pi
    
plt.plot(phi_o, Q, label='quad')
plt.plot(phi_o,T, label='trapecio')

plt.legend()
plt.show()

plt.clf()
plt.plot(phi_o, np.abs(Q-T_To),label = 'diferencia con quad')
plt.plot(phi_o, np.abs(T-T_To),label = 'diferencia con trapecio')


plt.legend()
plt.show()