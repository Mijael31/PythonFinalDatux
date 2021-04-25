##PROBLEMA 2 //CIFRADO DE CESAR
##Implemente un programa que encripte mensajes usando el cifrado de Caesar, según lo siguiente.

import string

cadena = string.ascii_lowercase

k = int(input('Introduzca k: '))
plaintext = input('Introduzca texto a cifrar: ')

ciphertext = ''
for l in plaintext:
    
    if l.lower() in cadena:
        p = cadena.find(l.lower())
        # algoritmo cesar
        c = (p + k) % 26
        
        if l.isupper():
            ciphertext += ciphertext.join(cadena[c].upper())
        else:
            ciphertext += ciphertext.join(cadena[c])
    else:
        ciphertext += ciphertext.join(l)
        
ciphertext