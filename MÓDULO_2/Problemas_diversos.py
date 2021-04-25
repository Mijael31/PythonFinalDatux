##PROBLEMAS DIVERSOS

##PROBLEMA1

#Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el
#nombre completo y permitir el ingreso de 3 notas. Las notas deben estar comprendidas entre 0 y 10. 
#Devolver el listado de alumnos

def ingresar_nota():
    
    try:
        nota = float(input("Digite una nota: "))
        
        if nota >=0 and nota <= 10:
            return nota
        else:
            print('La nota no es válida, debe estar comprendida entre 0 y 10')
            ingresar_nota()
    except:
        print("Introduzca una nota correcta")
        ingresar_nota()
        
def listar_alumnos(cantidad_alumnos):
    lista_alumnos = []
    for i in range(cantidad_alumnos):
        alumno = {}
        ##Ingresando de nombre de alumno
        alumno['nombre'] = input('Digite el nombre del alumno {}: '.format(i+1))

        ##Ingresando las notas
        alumno['nota1'] = ingresar_nota()
        alumno['nota2'] = ingresar_nota()
        alumno['nota3'] = ingresar_nota()
    
        ##Agregando los nombres de los alumnos
        lista_alumnos.append(alumno)
    
    return lista_alumnos

n = int(input('Digite la cantidad de alumnos a ingresar: '))
listado = listar_alumnos(n)
listado

## PROBLEMA2

# Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuántos desaprobaron, teniendo
# en cuenta que se aprueba con 4. La nota será el promedio de las 3 notas para cada alumno

def aprobados():
    m = int(input("Ingrese el numero de alumnos: "))
    listado = listar_alumnos(m)
    c=0
    for i in range(m):
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        Prom = (n1+n2+n3)/3
        if Prom < 4:
            c+=1
    print("La cantidad de alumnos aprobados es: {}".format(m-c))
    
aprobados()

##PROBLEMA3

# Informar el promedio de nota del curso total.

def promedio_curso(n):
    listado = listar_alumnos(n)
    c=0
    S=0
    Promedio=[]
    for i in range(n):
        
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        Prom = (n1+n2+n3)/3
        Promedio.append(Prom)
        
    for j in Promedio:
        S = S + j 
        
    
    Total = S / n

    
    print("El promedio final del curso es: {0:.3f}".format(Total))
    
promedio_curso(2)


##PROBLEMA4

# Realizar una función que indique quién tuvo el promedio más alto y quién tuvo la nota promedio más baja.

def promedio_max_min(n):
    listado = listar_alumnos(n)
    c=0
    Promedio=[]
    for i in range(n):
        
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        Prom = (n1+n2+n3)/3
        Promedio.append(Prom)
        
    maximo=max(Promedio)
    minimo=min(Promedio)
    a=Promedio.index(maximo)
    b=Promedio.index(minimo)
    
    print("El promedio más alto fue de: {}".format(listado[a]['nombre']))
    print("El promedio más bajo fue de: {}".format(listado[b]['nombre']))
        
promedio_max_min(2)

##PROBLEMA5

# Realizar una función que permita buscar un alumno por nombre, siendo el nombre completo o parcial, y devuelva
# una lista con los n alumnos que concuerden con ese nombre junto con todos sus datos, incluido el promedio de sus notas.

print(listado)

for i in range(len(listado)):
        
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        prom = round((n1+n2+n3)/3,3)
        listado[i]['Promedio'] = prom

listado


def Busqueda(texto):
    try:
        for i in range(3):
            if texto == listado[i]['nombre']:
                print(listado[i])
    except:    
        print("No se ha encontrado alumnos con ese nombre:")
            
Busqueda("mijael")


