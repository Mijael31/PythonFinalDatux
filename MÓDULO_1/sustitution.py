#PROBLEMA2
#Implemente un programa que implemente un cifrado de sustitución, acorde al ejercicio explicado.
def sustituye(texto):
    
    import string #Importando string para que ALFABETO funcione
    cadena = string.ascii_lowercase ##Definiendo la cadena
    
    clave = input("Ingrese la clave: ")
    texto_encriptado ="" ##Definiendo la cadena vacía en donde se ingresará el texto encriptado
    if len(clave)!=26:
        print("La clave debe tener 26 caracteres")
    elif not clave.isalpha():
        print("La clave presenta caracteres no alfabeticos")       
    else:
        for l in texto:
                    
            if l.lower() in cadena: ##Agregando texto a cadena
                c = cadena.find(l.lower())
        
                if l.isupper():
                    texto_encriptado += texto_encriptado.join(clave[c].upper())
                else:
                    texto_encriptado += texto_encriptado.join(clave[c].lower())
            else:
                texto_encriptado += texto_encriptado.join(l)
                
    print("Texto plano: ", texto)
    print("Texto encriptado: ", texto_encriptado)
    print("0")
            
sustituye("hello, world")