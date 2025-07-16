# 1.- Función que suma dos números
def sumar_dos_numeros(a, b):
    return a + b

# 2.- Función que calcula el área de un círculo
def area_de_circulo(radio):
    pi = 3.1416
    return pi * radio * radio

# 3.- Función que suma argumentos arbitrarios y valida que todos sean números
def sumar_todos_los_numeros(*args):
    for valor in args:
        if not isinstance(valor, (int, float)):
            return "Error: todos los elementos deben ser números"
    return sum(args)

# 4.- Convertir °C a °F
def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5.- Función que retorna la estación del año
def verificar_estacion(mes):
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes inválido'

# 6.- Función que calcula la pendiente (slope)
def calcular_pendiente(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Infinita (división por cero)"
    return (y2 - y1) / (x2 - x1)

# 7.- Resolver ecuación cuadrática
import cmath
def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminante) / (2*a)
    x2 = (-b - discriminante) / (2*a)
    return x1, x2

# 8.- Función que imprime los elementos de una lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

# 9.- Función que revierte una lista usando bucles
def revertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

# 10.- Capitalizar cada elemento de una lista
def capitalizar_lista(lista):
    return [elemento.capitalize() for elemento in lista]

# 11.- Agregar un ítem al final de una lista
def agregar_elemento(lista, item):
    lista.append(item)
    return lista

# 12.- Eliminar un ítem de una lista
def eliminar_elemento(lista, item):
    if item in lista:
        lista.remove(item)
    return lista

# 13.- Sumar todos los números desde 0 hasta el número dado
def suma_de_numeros(n):
    return sum(range(n + 1))

# 14.- Sumar solo los impares hasta el número dado
def suma_de_impares(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 15.- Sumar solo los pares hasta el número dado
def suma_de_pares(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
