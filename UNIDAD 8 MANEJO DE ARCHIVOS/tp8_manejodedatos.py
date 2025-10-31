#EJERCICIO1

with open ("productos.txt", "w") as archivo:
    archivo.write("cartera,2500,10\n")
    archivo.write("llavero,800,25\n")
    archivo.write("billetera,3000,15\n")

#EJERCICIO2

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cant = linea.strip().split(",")

#EJERCICIO3

print ("Agregar nuevo producto")
nuevo_nombre = input("Ingrese el nombre del producto:")
nuevo_precio = input("Ingrese el precio:")
nueva_cant = input("Ingrese la cantidad:")

with open("productos.txt", "a") as archivo:
    archivo.write(f"\n{nuevo_nombre},{nuevo_precio},{nueva_cant}")
    print("Producto agregado correctamente")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip() 

        partes = linea.split(",")
        if len(partes) == 3:
            nombre, precio, cant = partes
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cant}")
        else:
            print(f"Línea inválida: {linea}")

#EJERCICIO4

productos = []  

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        if len(partes) == 3:
            nombre, precio, cant = partes
            # Creamos un diccionario para cada producto
            producto = {
                "nombre": nombre,
                "precio": precio,      # lo convertimos a número
                "cantidad": cant      # lo convertimos a número
            }
            productos.append(producto)  # lo agregamos a la lista

# Mostramos la lista completa
print("Lista de productos cargados:")
for p in productos:
    print(p)

#EJERCICIO5

buscar = input("Ingrese el nombre del producto que desea buscar: ")

encontrado = False  # bandera para saber si lo encontramos

for p in productos:
    if p["nombre"].lower() == buscar.lower():  # comparación sin importar mayúsculas
        print(f"Producto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: el producto no existe en la lista.")

#EJERCICIO6

with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("✅ Archivo actualizado correctamente.")
