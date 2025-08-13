#EJERCICIO 1
print("Hola mundo!")

#EJERCICIO 2
nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!")

#EJERCICIO 3
nombre = input("Ingrese su nombre: ")
apellido = input(f"{nombre}, ingrese su apellido: ")

nombre_completo = nombre +" "+ apellido
edad = input (f"{nombre_completo}, ingrese su edad: ")
lugar = input (f"{nombre_completo}, ingrese su lugar de residencia: ")

print (f"Soy {nombre_completo}, tengo {edad} años y vivo en {lugar}.")

#EJERCICIO 4
pi = 3.14159
radio = input("Ingrese el radio del circulo: ")
radio = int(radio)
area = (radio ** 2) * pi
perimetro = 2 * pi * radio
print (f"El area del circulo con radio de {radio} es igual a {area} y su perimetro es {perimetro}")

#EJERCICIO 5
segs = input("Ingrese una cantidad de segundos para pasarlo a horas: ")
segs = int(segs)
horas = segs / 3600
print (f"{segs} equivale a {horas}")

#EJERCICIO 6
num = input ("Ingrese un número: ")
num = int(num)
print (f"{num} x 1 = {num*1}, {num} x 2 = {num*2}, {num} x 3 = {num*3}, {num} x 4 = {num*4}, {num} x 5 = {num*5}, {num} x 6 = {num*6}, {num} x 7 = {num*7}, {num} x 8 = {num*8}, {num} x 9 = {num*9}, {num} x 10 = {num*10}")

#EJERCICIO 7
num1 = input("Ingrese el primer número (debe ser distinto 0): ")
num2 = input("Ingrese el segundo número (debe ser distinto 0): ")
num1 = int(num1)
num2 = int(num2)
print (f"La suma de {num1} y {num2} es {num1+num2}")
print (f"La resta de {num1} y {num2} es {num1-num2}")
print (f"La multiplicación entre {num1} y {num2} es {num1*num2}")
print (f"La división entre {num1} y {num2} es {num1/num2}")

#EJERCICIO 8
altura = input("Ingrese su altura: ")
peso = input("ingrese su peso: ")
altura = int(altura)
peso = int(peso)
imc = peso / (altura ** 2)
print(f"Tu IMC es {imc}")

#EJERCICIO 9
temp = input("Ingrese un temperatura en grados Celcius: ")
temp = int(temp)
print (f"El equivalente de {temp} en Farenheit es igual {(temp * 9) / 5 + 32}")

#EJERCICIO 10   
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
num3 = input("Ingrese el tercer número: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
print(f"El promedio de {num1}, {num2}, {num3} es {(num1+num2+num3)/3}")