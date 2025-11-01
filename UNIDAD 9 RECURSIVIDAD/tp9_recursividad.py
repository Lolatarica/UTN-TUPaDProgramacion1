#EJERCICIO1 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

#EJERCICIO2

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingrese la cantidad de términos: "))
for i in range(n):
    print(fibonacci(i), end=" ")

#EJERCICIO3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")

#EJERCICIO4

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(num)
print(f"El número {num} en binario es: {resultado if resultado else '0'}")

#EJERCICIO5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")

#EJERCICIO6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número: "))
print(f"La suma de los dígitos es: {suma_digitos(num)}")

#EJERCICIO7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese el número de bloques del nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

#EJERCICIO8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("Ingrese un número: "))
d = int(input("Ingrese el dígito a buscar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces.")




