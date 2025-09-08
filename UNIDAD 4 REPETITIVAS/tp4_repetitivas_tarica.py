#EJERCICIO 1
for num in range (0,101):
    print(num)
    num += 1

print("////")
#EJERCICIO 2
numero = int(input("Ingrese un número entero: "))
n = numero

if numero == 0:
    digitos = 1
else:
    digitos = 0
    while n > 0:
        n //= 10   
        digitos += 1

print(f"El número {numero} tiene {digitos} dígitos.")

print("////")
#EJERCICIO 3
num1 = int(input("Ingrese un numero entero:"))
num2 = int(input("Ingrese otro numero entero: "))
suma = 0

for cont in range (num1+1,num2):
    suma += cont

print(f"La suma de todos los numeros enteros entre {num1} y {num2} es: {suma}")

print("////")
#EJERCICIO 4
CORTE = 0
num = int(input(f"Ingrese un numero entero ({CORTE} para cortar): "))
suma = 0

while num != CORTE:
    suma += num
    num = int(input(f"Ingrese un numero entero ({CORTE} para cortar): "))

print(f"La suma total de los numeros ingresados es: {suma}")

print("////")
#EJERCICIO 5
CORTE = 10

import random

num_alea = random.randint(0, 9)  
num = int(input(f"Adivine el numero entre el 0 al 9 ({CORTE} para cortar): "))

while num != CORTE:
    if num == num_alea:
        print(f"Adivinaste el {num} era el correcto!")
        num_alea = random.randint(0, 9)  
    else:
        print(f"{num} no era el numero correcto. Intenta de vuelta!")
    num = int(input(f"Adivine el numero entre el 0 al 9 ({CORTE} para cortar): "))

print ("Gracias!")

print("////")
#EJERCICIO 6
for num in range (100,-2,-2):
    print(num)
    num += 1

print("////")
#EJERCICIO 7
num = int(input("Ingrese un numero entero: "))
suma = 0

if num >= 0:
    for cont in range (0,num):
        suma += cont
else:
    print("El numero debe ser positivo")

print(f"La suma de todos los numeros enteros entre 0 y {num} es: {suma}")

print("////")
#EJERCICIO 8
num_p = 0
num_n = 0
num_pa = 0
num_im = 0

for cont in range(1,101):
    num = int(input(f"Ingrese el numero entero {cont}: "))
    if num >= 0:
        num_p += 1
    else:
        num_n += 1
    
    if num % 2 == 0:
        num_pa += 1
    else:
        num_im += 1
 
print(f"Entre los numero ingresados hay {num_p} numeros positivos, {num_n} numero negativos, {num_pa} numero pares y {num_im} numeros impares")

print("////")
#EJERCICIO 9
suma = 0

for cont in range(1,101):
    num = int(input(f"Ingrese el numero entero {cont}: "))
    suma += num

media = suma/cont

print(f"La media de todos los numeros ingresados es {media}")

print("////")
#EJERCICIO 10
num = int(input(f"Ingrese un numero entero: "))
nuevo_num = 0

while num > 0:
    ultimo = num % 10       
    num = num // 10      
    nuevo_num = nuevo_num * 10 + ultimo  

print(f"Número invertido: {nuevo_num}")

