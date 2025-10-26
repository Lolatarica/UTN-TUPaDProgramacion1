#EJERCICIO 1
def imprimir_hola_mundo():
    print ("Hola Mundo!")

imprimir_hola_mundo()

#EJERCICIO 2
def saludar_usuario(nombre):
    print (f"Hola {nombre}!")

nombre = input("Ingrese su nombre:")
saludar_usuario(nombre)

#EJERCICIO 3
def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

usuario = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese su residencia:")

informacion_personal(usuario, apellido, edad, residencia)

#EJERCICIO 4
def calcular_area_circulo(radio):
    return (radio ** 2) * 3.14

def calcular_perimetro_circulo(radio):
    return (radio * 2) * 3.14

radio = int(input("Ingrese el radio del circulo:"))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print (f"El area del circulo es {area} y el perimetro {perimetro}")
 
#EJERCICIO 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese una cantidad de segundos:"))
print(segundos_a_horas(segundos))

#EJERCICIO 6
def tabla_multiplicar(numero):
    for i in range (11):
        print (f"{numero} x {i} = {numero*i}")

num = int(input("Ingrese un numero:"))
tabla_multiplicar(num)

#EJERCICIO 7
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a/b
    else:
        division = "No se puede dividir por 0"
    
    return (suma, resta, multiplicacion, division)

a = int(input("Ingres el primer numero:"))
b = int(input("Ingres el segundo numero:"))

resultado = operaciones_basicas(a,b)

suma = resultado[0]
resta = resultado[1]
multiplicacion = resultado[2]
division = resultado[3]

print(f"{a} + {b} = {suma}")
print(f"{a} - {b} = {resta}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division}")

#EJERCICIO 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)
print(f"Su IMC es: {resultado}")
    
#EJERCICIO 9
def celsius_a_farenheit(celsius):
    return (celsius * 9/5) + 32

grados = float(input("Ingrese una temperatura en celsius"))
print(f"Equivalente de {grados} celsius a Farenheit es: {celsius_a_farenheit(grados)}")

#EJERCICIO 10
def calcular_promedio(a,b,c):
    return (a+c+b)/3

nota1 = int(input("Ingrese la primera nota:"))
nota2 = int(input("Ingrese la segunda nota:"))
nota3 = int(input("Ingrese la tercera nota:"))

print(calcular_promedio(nota1,nota2,nota3))


