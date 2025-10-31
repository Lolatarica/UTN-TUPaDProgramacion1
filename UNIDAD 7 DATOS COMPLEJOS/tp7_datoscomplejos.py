#EJERCICIO 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#EJERCICIO 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

#EJERCICIO 3

frutas = list(precios_frutas.keys())
print(frutas)

#EJERCICIO 4
contactos = {}

for cont in range(5):
    nombre = input("Ingrese un nombre de contacto:")
    numero = input("Ingrese el número telefonico:")

    contactos[nombre] = numero

contacto = input("Ingrese un nombre para buscar el contacto:")

if contacto in contactos:
    print("El número de", contacto, "es:", contactos[contacto])
else:
    print("No se encontró el contacto.")

#EJERCICIO 5

frase = input("Ingrese una frase: ")

# Separamos la frase en palabras
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(conteo_palabras)

#EJERCICIO 6

alumnos = {}

for i in range(3):
    alumno = input("Ingrese el nombre del alumno:")
    nota1 = int(input("Ingrese la primera nota:"))
    nota2 = int(input("Ingrese la segunda nota:"))
    nota3 = int(input("Ingrese la tercera nota:"))

    notas = (nota1, nota2, nota3)
    alumnos[alumno] = notas

print ("Promedio de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:2f}")

#EJERCICIO 7

parcial1 = {"Ana", "Luis", "María", "Sofía", "Juan"}
parcial2 = {"Luis", "María", "Pedro", "Carla", "Juan"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#EJERCICIO 8

productos = {
    "Pan": 50,
    "Facturas": 30,
    "Tortas": 10,
    "Galletas": 40
}

producto = input("Ingrese el nombre del producto: ")

if producto in productos:
    print(f"Stock actual de {producto}: {productos[producto]} unidades")
    
    agregar = int(input("Ingrese cuántas unidades desea agregar: "))
    productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {productos[producto]} unidades")

else:
    print(f"El producto '{producto}' no existe en el inventario.")
    nuevo_stock = int(input("Ingrese el stock inicial para agregarlo: "))
    productos[producto] = nuevo_stock
    print(f"Se agregó el producto '{producto}' con {nuevo_stock} unidades.")

print("Inventario actualizado:")
print(productos)

#EJERCICIO 9

agenda = {}
 
for i in range(3):
    dia = input("Ingrese el dia del evento:")
    hora = input("Ingrese la hora del evento:")
    evento = input("Ingrese el nombre del evento:")

    key = (dia,hora)
    agenda[key] = evento

print("Agenda:")
for key, evento in agenda.items():
    print(f"{key}: {evento}")
    
#EJERCICIO 10

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Paraguay": "Asunción"
}

capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario original (País → Capital):")
print(paises)

print("\nDiccionario invertido (Capital → País):")
print(capitales)