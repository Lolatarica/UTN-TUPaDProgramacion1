#EJERCICIO 1
edad = int(input("Ingrese su edad:"))

if edad > 18:
    print("Es mayor de edad")

#EJERCICIO 2
nota = int(input("Ingrese su nota:"))

if nota >= 6:
    print("Aprobado")
else:
    print("Desarobado")

#EJERCICIO 3
num = int(input("Ingrese un numero par:"))

if (num % 2) == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#EJERCICIO 4
edad = int(input("Ingrese su edad:"))

if edad < 12:
    print("Su categoria es: Niño/a")
elif edad >= 12 and edad < 18:
    print("Su categoria es: Adolescente")
elif edad >= 18 and edad < 30:
    print("Su categoria es: Adulto/a joven")
else:
    print("Su categoria es: Adulto/a")

#EJERCICIO 5
contrasena = input("Ingrese una contrasena:")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraena de entre 8 y 14 caracteres")

#EJERCICIO 6
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print(numeros_aleatorios)
    print(moda)
    print(mediana)
    print(media)
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print(numeros_aleatorios)
    print(moda)
    print(mediana)
    print(media)
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print(numeros_aleatorios)
    print(moda)
    print(mediana)
    print(media)
    print("Sin sesgo")
else:
    print(numeros_aleatorios)
    print(moda)
    print(mediana)
    print(media)
    print("No cumple estrictamente con ningún sesgo del enunciado")

#EJERCICIO 7
frase_palabra = input("Ingrese una frase o palabra:")

ultimo = frase_palabra[-1].lower()

if ultimo == "a" or ultimo == "e" or ultimo == "i" or ultimo == "o" or ultimo == "u":
    frase_palabra += "!"
    print(frase_palabra)
else:
    print(frase_palabra)

#EJERCICIO 8
nombre = input("Ingrese su nombre:")
print("Como quiere su nombre?")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = input("Ingrese la opcion deseada:")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("No se seleccion correctamente una opcion. Escriba el numero de la misma")

#EJERCICIO 9
magnitud = int(input("Ingrese la magnitud del terremoto:"))

if magnitud < 3:
    print("Muy leve. Imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("Leve. Ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado. Sentido por personas, pero generalmente no causa daños")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte. Puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte. Puede causar daños significativos")
else:
    print("Extremo. Puede causar graves daños a gran escala")

#EJERCICIO 10
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese número de mes (1-12): "))
dia = int(input("Ingrese día del mes: "))

estacion = ""

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"

print(f"Estás en {estacion}")

