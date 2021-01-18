# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:47:24 2021

@author: Ricardo Vargas
"""

   
import itertools

def rutas(ciudades,inicio,fin):
    validas=[]
    opciones=itertools.permutations(ciudades,5)
    for i in opciones:
        if(i[0]==inicio and i[4]==fin):
            validas.append(i)
    print(f"El numero de rutas disponibles es: {len(validas)}")
    print()
    return validas

def listarrutas(opciones):
    for i in opciones:
        print(f"Ruta {i}")
        
def suma(routes,opcion):
    s=0
    print("---------------")
    for i in range(len(opcion)-1):
        print(opcion[i],"->",opcion[i+1],end='=')
        print(routes[opcion[i]-1][opcion[i+1]-1])
        s=s+routes[opcion[i]-1][opcion[i+1]-1]
    print(f"El costo de la ruta es: {s}")
    return s

def rutaMayor(routes,opciones):
    j=[]
    m=[]
    for i in range(len(opciones)):
        m.append(suma(routes, opciones[i]))
    mayor=max(m)
    for i in range(len(m)):
        if(m[i]>=mayor):
            j.append(i)
    print(f"\nEl mayor costo es: {mayor}\n")
    print("En la(s) ruta(s): ")
    for i in range(len(j)):
        print({opciones[j[i]]})
    
    
 
def rutaMenor(routes,opciones):
    j=[]
    m=[]
    for i in range(len(opciones)):
        m.append(suma(routes, opciones[i]))
    menor=min(m)
    for i in range(len(m)):
        if(m[i]<=menor):
            j.append(i)
    print(f"\nEl menor costo es: {menor}\n")
    print("En la(s) ruta(s): ")
    for i in range(len(j)):
        print({opciones[j[i]]})
        
def main():
    routes=((0,10,55,25,45),(10,0,20,25,40),(55,20,0,15,30),(25,25,15,0,50),(45,40,30,50,0))
    ciudades=(1,2,3,4,5)
    #print(suma(routes,ciudades))
    inicio=int(input("Nodo de inicio:"))
    fin=int(input("Nodo de destino:"))
    print()
    opciones=rutas(ciudades,inicio,fin)
    print("Las rutas disponibles son:")
    listarrutas(opciones)
    print()
    print("Costos de rutas:")
    rutaMayor(routes, opciones)
    print()
    print("Rutas de menor costo")
    rutaMenor(routes, opciones)

    return 0

main()