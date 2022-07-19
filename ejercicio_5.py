# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
primera= palabra_1[0:3]
# De la segunda palabra tome las primeras dos letras, utilice el operador :
segunda = palabra_2[0:2]
# Formar una nueva palabra con los recortes solicitados
resultado = primera + segunda
resultado2 = segunda + primera
resultado3 = segunda + segunda
resultado4 = primera + primera 

# Imprima en pantalla los resultados
print("COMBINACION DE PALABRAS: "+ "\n" + resultado +"\n"+resultado2+"\n"+resultado3+"\n"+resultado4)