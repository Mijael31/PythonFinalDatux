##PROBLEMAS_DIVERSOS

##PROBLEMA1

monto = float(input("Ingrese el monto inicial: "))
for i in range(1,4,1):
    monto = monto + monto*(4/100)
    print(f"Para el año {i} el monto será {round(monto,2)}")

##PROBLEMA2

a = int(input("Ingrese el coeficiente a: "))
b = int(input("Ingrese el coeficiente b: "))
c = int(input("Ingrese el coeficiente c: "))

if a != 0
    discrim = (b*b) - 4*(a*c)

if discrim > 0:
    x_1 = (-b + math.sqrt(discrim))/(2*a)
    x_2 = (-b + math.sqrt(discrim))/(2*a)
    print(f"La primera solución es {x_1} y la segunda {x_2}")
elif discrim == 0:
    x_1 -b/(2*a)
    print(f"Se tiene una solución doble con valor {x_1}")
else:
    print("La ecuación no presenta solución real")
