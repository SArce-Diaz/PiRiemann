#!/usr/bin/env python

def arctan(x):
    return 4/(1+x**2)#funcion que al integrarla da como resultado pi

def Riemann(valorInicial,valorFinal,iteraciones,funcion): #suma de Riemann
    cont = 0.0
    ancho = (valorFinal-valorInicial)/iteraciones #ancho de los rectángulos
    puntoMedio = (ancho/2) + valorInicial #forma del punto medio
    for i in range(iteraciones): #ciclo para efectuar la suma de Riemann
        cont += funcion(puntoMedio)
        puntoMedio += ancho
    cont *= ancho
    return cont

print(Riemann(0,1,1234567,arctan))
