#EJERCICIO 1
notas = [7.5, 10, 8.5, 8, 9, 8, 5, 5, 6.5, 9]

print ("Notas de los estudiantes: ")
for nota in notas:
    print (nota)

suma_notas = 0
for nota in notas:
    suma_notas += nota

promedio_notas = suma_notas / len(notas)

print (f"El promedio de las notas de los estudiantes es {promedio_notas}")

nota_max = notas[0]
nota_min = notas[0]

for nota in notas:
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

print (f"La nota mayor es {nota_max} y la menor {nota_min}")
#EJERCICIO 2
productos = []

for cont in range(1, 6):
    prod = input(f"Ingrese el producto {cont}: ")
    productos.append (prod)

productos = sorted(productos)

print ("Que producto desea eliminar?")
print ("Notas de los estudiantes: ")

numero = 1
for producto in productos:
    print (f"{numero} {producto}")
    numero += 1
           
eleccion = int(input("Ingrese el número del producto que desea eliminar: "))
if 1 <= eleccion <= len(productos):
    productos.remove(productos[eleccion-1])
    print("Lista actualizada:", productos)
else:
    print("Número inválido.")

#EJERCICIO 3
import random

numeros_azar = []

for i in range(15):
    numero = random.randint(1, 100)  # número entero entre 1 y 100
    numeros_azar.append(numero)

print("Lista de números aleatorios:")
for numero_azar in numeros_azar:
    print(numero_azar)

numeros_pares = []
numeros_impares = []

for numero_azar in numeros_azar:
    if numero_azar % 2 == 0:
        numeros_pares.append(numero_azar)
    else:
        numeros_impares.append(numero_azar)

print(f"Lista de números aleatorios pares ({len(numeros_pares)}):")
for numero_par in numeros_pares:
    print(numero_par)

print(f"Lista de números aleatorios impares ({len(numeros_impares)}):")
for numero_impar in numeros_impares:
    print(numero_impar)

#EJERCICIO 4
datos =  [1, 3, 5, 3, 7, 1, 9, 5, 3]

print ("Lista original: ")
for dato in datos:
    print(dato)

datos_norepetidos = []
for dato in datos:
    if dato not in datos_norepetidos:
        datos_norepetidos.append(dato)

print ("Lista sin datos repetidos: ")
for dato_norepetido in datos_norepetidos:
    print(dato_norepetido)

#EJERCICIO 5
alumnos_presentes = ["Juan", "Manuel", "Mariana", "Agustin", "Florencia", "Marta", "Joaquin", "Miguel"]

numero_alumno = 1
for alumno_presente in alumnos_presentes:
    print(f"{numero_alumno}. {alumno_presente}")
    numero_alumno +=1

print ("Desea eliminar o agregar a un alumno?")
print ("1. Agregar alumno.")
print ("2. Eliminar alumno.")
print ("3. Continuar sin accion.")
accion = input("Ingrese un numero del 1 al 3: ")

if accion == "1":
    nuevo = input("Ingrese el nombre del nuevo alumno: ")
    alumnos_presentes.append(nuevo)
    print(f"Alumno {nuevo} agregado correctamente.")
elif accion == "2":
    num = int(input("Ingrese el número del alumno que desea eliminar: "))
    if 1 <= num <= len(alumnos_presentes):
        eliminado = alumnos_presentes.remove(alumnos_presentes[num-1])
        print(f"Alumno {eliminado} eliminado correctamente.")
    else:
        print("Número inválido.")
elif accion == "3":
    print("No se realizaron cambios en la lista.")

else:
    print("Opción inválida.")

print("Lista final de alumnos presentes:")
numero_alumno = 1
for alumno_presente in alumnos_presentes:
    print(f"{numero_alumno}. {alumno_presente}")
    numero_alumno +=1

#EJERCICIO 6

lista = [3, 4, 5, 2, 88, 6, 5]

print("Lista original:", lista)

ultimo = lista[-1]

for i in range (len(lista)-1, 0, -1):
    lista[i] = lista[i-1]

lista[0] = ultimo

print (f"Lista rotada: {lista}")


#EJERCICIO 7

temperaturas = [
    [23, 13],
    [23, 12],
    [21, 12],
    [17, 10],
    [23, 13],
    [25, 18],
    [18, 12]
]

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Temperaturas de la semana:\n")

for i in range(len(dias)):
    print(dias[i], " Máx:", temperaturas[i][0], "° / Mín:", temperaturas[i][1], "°")

suma_min = 0
suma_max = 0

for temperatura in temperaturas:
    suma_min += temperatura[1]
    suma_max += temperatura[0]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print (f"Promedio de temperaturas maximas: {round(promedio_max)}°")
print (f"Promedio de temperaturas minimas: {round(promedio_min)}°")


mayor_amplitud = 0
dia = ""

for i in range(len(temperaturas)):
    min_temp = temperaturas[i][1]
    max_temp = temperaturas[i][0]
    amplitud = max_temp - min_temp
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia = dias[i]

print(f"El dia con la mayor amplitud fue {dia} con {mayor_amplitud}°")

#EJERCICIO 8

notas = [
    ["Matematica", 5, 6, 9, 10, 8],
    ["Geografia", 7, 6, 7, 9, 5],
    ["Lengua", 2, 7, 8, 7, 7]
    ]

print ("Promedio en cada materia: ")
for nota in notas:
    materia = nota[0]
    calificaciones = nota[1:]
    total = 0
    for calificacion in calificaciones:
        total += calificacion
    promedio = total / len(calificaciones)
    print (f"{materia}: {round(promedio)}")

print ("Promedio de cada estudiante:")
num_estudiantes = len(notas[0]) - 1

for i in range(num_estudiantes):
    total = 0
    for nota in notas:
        total += nota[i+1]
    promedio = total /len(notas)
    print (f"Estudiante {i+1}: {round(promedio)}")

#EJERCICIO 9

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
    ]

for fila in tablero:
    for celda in fila:
        print (celda, end= " ")
    print()

jugador = "x"
jugadas = 0

while jugadas < 9:
    print(f"Turno del jugador {jugador}")
    fila = int(input("ingrese la fila seleccionada:(0-2) "))
    columna = int(input("ingrese la columna seleccionada:(0-2) "))

    if fila<0 or fila>2 or columna<0 or columna>2:
        print ("Fuera de rango")
        continue
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas += 1
    else:
        print ("Esa casilla esta ocupada.")
    
    for fila in tablero:
        for celda in fila:
            print (celda, end= " ")
        print()

    if jugador == "x":
        jugador = "o"
    else:
        jugador = "x"

#EJERCICIO 10

ventas = [
    [12,3,23,43,22,12,2],
    [2,3,0,1,6,2,2],
    [34,33,27,22,23,28,33],
    [12,3,23,43,22,12,2]
]

print ("Total de productos vendidos: ")
totales_prods = 0
for i in range(4):
    total = 0
    for j in range (7):
        total += ventas[i][j]
    totales_prods.append(total)
    print(f"Producto {i+1}: {total}")


print("Ventas totales por día:")
totales_dias = []
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)
    print(f"Día {j+1}: {total_dia}")

mayor_ventas = totales_dias[0]
dia_max = 1
for j in range(1, 7):
    if totales_dias[j] > mayor_ventas:
        mayor_ventas = totales_dias[j]
        dia_max = j+1

print(f"El día con mayores ventas fue el Día {dia_max} ({mayor_ventas} ventas).")

mayor_prod = totales_prods[0]
prod_max = 1
for i in range(1, 4):
    if totales_prods[i] > mayor_prod:
        mayor_prod = totales_prods[i]
        prod_max = i+1

print(f"El producto más vendido fue el Producto {prod_max} ({mayor_prod} ventas).")
