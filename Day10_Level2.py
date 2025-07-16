# 1.- Usar un bucle for para iterar de 0 a 100 y mostrar la suma de todos los números
suma_total = 0
for numero in range(101):
    suma_total += numero
print("La suma de todos los números es", suma_total)  # Resultado esperado: 5050

# 2.- Usar un bucle for para sumar pares e impares por separado
suma_pares = 0
suma_impares = 0

for numero in range(101):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("La suma de todos los números pares es", suma_pares)     # Resultado esperado: 2550
print("La suma de todos los números impares es", suma_impares) # Resultado esperado: 2500