# 1.- Iterar de 0 a 10 usando for
for numero in range(11):
    print(numero)

# 1.- Iterar de 0 a 10 usando while
numero = 0
while numero <= 10:
    print(numero)
    numero += 1

# 2.- Iterar de 10 a 0 usando for
for numero in range(10, -1, -1):
    print(numero)

# 2.- Iterar de 10 a 0 usando while
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

# 3.- Imprimir triángulo con 7 líneas
for i in range(1, 8):
    print('#' * i)

# 4.- Imprimir cuadrícula de 8x8 con bucles anidados
for fila in range(8):
    for columna in range(8):
        print('#', end=' ')
    print()  # Salto de línea después de cada fila

# 5.- Imprimir patrón de multiplicación
for numero in range(11):
    print(f"{numero} x {numero} = {numero * numero}")

# 6.- Iterar y mostrar elementos de la lista
tecnologias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tecnologia in tecnologias:
    print(tecnologia)

# 7.- Imprimir números pares del 0 al 100
for numero in range(0, 101):
    if numero % 2 == 0:
        print(numero)

# 8.- Imprimir números impares del 0 al 100
for numero in range(0, 101):
    if numero % 2 != 0:
        print(numero)