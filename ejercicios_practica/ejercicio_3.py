# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

nombre_completo = nombre +" "+ apellido
# Imprima su nombre completo
print ("El nombre y apellido ingresado es: ",nombre_completo)
# Almacenar su nombre completo en una variable
# nombre_completo = .....

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letras= len(nombre_completo)-1

print("Su nombre completo tiene ",cantidad_letras, " letras que lo componen")