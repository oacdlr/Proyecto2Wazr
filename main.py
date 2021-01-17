import itertools
def rutas(ciudades,inicio,fin):
    validas=[]
    opciones=itertools.permutations(ciudades,5)
    for i in opciones:
        if(i[0]==inicio and i[4]==fin):
            validas.append(i)
    return validas
def listarrutas(opciones):
    for i in opciones:
        print(i)
def suma(routes,opcion):
    s=0
    for i in range(len(opcion)-1):
        print(opcion[i],"->",opcion[i+1],end='/')
        print(routes[opcion[i]-1][opcion[i+1]-1])
        s=s+routes[opcion[i]-1][opcion[i+1]-1]
    return s
def main():
    routes=((0,10,55,25,45),(10,0,20,25,40),(55,20,0,15,30),(25,25,15,0,50),(45,40,30,50,0))
    ciudades=(1,2,3,4,5)
    print(suma(routes,ciudades))
    inicio=int(input("Nodo de inicio"))
    fin=int(input("Nodo de destino"))
    opciones=rutas(ciudades,inicio,fin)
    listarrutas(opciones)
    return 0
main()
