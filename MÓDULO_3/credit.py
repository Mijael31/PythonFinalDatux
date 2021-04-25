#PROBLEMA C´REDITO

# Implemente un programa que determine si un número de tarjeta de crédito proporcionado es válido según el algoritmo de Luhn.

def algoritmo_luhn():
    
    n= input("Ingrese el número de su tarjeta: ")

    suma = 0
    alt = 0
    i = len(n) - 1
    valor = 0
    
    while i >= 0:
       valor = int( n[ i ] )

       if alt:
          valor = valor * 2
          if valor > 9:
             valor = ( valor % 10 ) + 1  

       suma = suma + valor
 
       alt = not alt 
       i -= 1

# Imprimiendo el tipo de tarjeta que es
        
    if suma%10 == 0 and n[0] == "4" :
        print("VISA")
    elif suma%10 == 0 and n[0] == "3" :
        print("AMEX")
    elif suma%10 == 0 and n[0] == "5" :
        print("MASTERCARD")
    else :
        print("La digitación de la tarjeta es incorrecta")
        
algoritmo_luhn()