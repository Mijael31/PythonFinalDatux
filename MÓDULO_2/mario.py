##PROBLEMA 1 // JUEGO DE MARIO

## Implemente un programa que imprima una media pirámide de una altura específica, como se indica a continuación.
altura = input("Ingrese la altura de la pirámide (entre 1 y 8): ")

if not altura.isnumeric(): ##Validando altura numérica
    print("La altura no es correcta, debe ingresar un dato numérico")
elif int(altura) < 1 or int(altura) > 8:
    print("La altura no es correcta, debe ingresar un dato numérico entre el 1 y 8")
else:
    for i in range(int(altura)):
        print(" " * (int(altura)-i-1) + "#" * (i+1))