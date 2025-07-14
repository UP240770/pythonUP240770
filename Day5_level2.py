# 1.- Lista de edades de estudiantes
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista
edades.sort()
print("Edades ordenadas:", edades)

# Encontrar edad mínima y máxima
edad_min = min(edades)
edad_max = max(edades)
print("Edad mínima:", edad_min)
print("Edad máxima:", edad_max)

# Agregar edad mínima y máxima nuevamente a la lista
edades.append(edad_min)
edades.append(edad_max)
print("Edades con min y max añadidas:", edades)

# Calcular la mediana
edades.sort()
n = len(edades)
if n % 2 == 0:
    mediana = (edades[n // 2 - 1] + edades[n // 2]) / 2
else:
    mediana = edades[n // 2]
print("Mediana de edades:", mediana)

# Calcular el promedio
promedio = sum(edades) / len(edades)
print("Promedio de edades:", promedio)

# Rango de edades
rango = edad_max - edad_min
print("Rango de edades:", rango)

# Comparación de |min - promedio| y |max - promedio|
diferencia_min = abs(edad_min - promedio)
diferencia_max = abs(edad_max - promedio)
print("Diferencia entre min y promedio:", diferencia_min)
print("Diferencia entre max y promedio:", diferencia_max)

# 2.- Encontrar el país del medio en la lista de países
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
indice_medio = len(paises) // 2
if len(paises) % 2 == 0:
    paises_medio = [paises[indice_medio - 1], paises[indice_medio]]
else:
    paises_medio = [paises[indice_medio]]
print("País(es) del medio:", paises_medio)

# 3.- Dividir la lista de países en dos mitades
if len(paises) % 2 == 0:
    mitad1 = paises[:len(paises)//2]
    mitad2 = paises[len(paises)//2:]
else:
    mitad1 = paises[:len(paises)//2 + 1]
    mitad2 = paises[len(paises)//2 + 1:]
print("Primera mitad de países:", mitad1)
print("Segunda mitad de países:", mitad2)

# Desempaquetar los tres primeros países y el resto como países escandinavos
pais1, pais2, pais3, *escandinavos = paises
print("País 1:", pais1)
print("País 2:", pais2)
print("País 3:", pais3)
print("Países escandinavos:", escandinavos)
