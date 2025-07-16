# 1.- Función que cuenta pares e impares hasta un número dado
def evens_and_odds(numero):
    pares = 0
    impares = 0
    for i in range(numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"The number of odds are {impares}.")
    print(f"The number of evens are {pares}.")

# 2.- Función que calcula el factorial de un número
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

# 3.- Función que verifica si un parámetro está vacío
def is_empty(valor):
    if valor:
        return False
    return True

# 4-1.- Calcular la media de una lista
def calcular_media(lista):
    return sum(lista) / len(lista)

# 4-2.- Calcular la mediana
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]

# 4-3.- Calcular la moda
from collections import Counter
def calcular_moda(lista):
    frecuencias = Counter(lista)
    max_frecuencia = max(frecuencias.values())
    modas = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
    return modas

# 4-4.- Calcular el rango (máximo - mínimo)
def calcular_rango(lista):
    return max(lista) - min(lista)

# 4-5.- Calcular la varianza
def calcular_varianza(lista):
    media = calcular_media(lista)
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    return suma_cuadrados / len(lista)

# 4-6.- Calcular desviación estándar
import math
def calcular_std(lista):
    return math.sqrt(calcular_varianza(lista))
