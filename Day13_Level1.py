# 1.- Filtrar solo negativos y ceros en la lista usando list comprehension
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numeros if n <= 0]
print("1:", negativos_y_ceros)

# 2.- Aplanar lista de listas de listas a una lista unidimensional
listas_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [numero for sublista in listas_de_listas for fila in sublista for numero in fila]
print("2:", lista_aplanada)

# 3.- Crear una lista de tuplas con potencias
lista_de_tuplas = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print("3:", lista_de_tuplas)

# 4.- Aplanar lista de países a una nueva lista con formato personalizado
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista_formateada = [[pais.upper(), pais[:3].upper(), ciudad.upper()] for [[(pais, ciudad)]] in paises]
print("4:", lista_formateada)

# 5.- Cambiar la lista a una lista de diccionarios
lista_diccionarios = [{'country': pais.upper(), 'city': ciudad.upper()} for [[(pais, ciudad)]] in paises]
print("5:", lista_diccionarios)

# 6.- Cambiar la lista de listas a una lista de cadenas concatenadas
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_concatenados = [f"{nombre} {apellido}" for [[(nombre, apellido)]] in nombres]
print("6:", nombres_concatenados)

# 7.- Función lambda para calcular la pendiente y el intercepto de funciones lineales
# Pendiente: m = (y2 - y1) / (x2 - x1)
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
# Intercepto: b = y - mx
intercepto = lambda x, y, m: y - m * x

# Ejemplo de uso
m = pendiente(1, 2, 3, 6)         # Debe ser 2.0
b = intercepto(1, 2, m)           # Debe ser 0.0
print("7: pendiente =", m, ", intercepto =", b)
