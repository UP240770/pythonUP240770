# Paso 1: Desempaquetar hermanos y padres desde family_members
miembros_familia = ('Aurora', 'Natalia', 'Alex', 'Adrian', 'Paty', 'Felipe')
hermanos_y_hermanas, mama, papa = miembros_familia
print("Hermanos y hermanas:", hermanos_y_hermanas)
print("Mamá:", mama)
print("Papá:", papa)

# Paso 2: Crear tuplas de frutas, vegetales y productos animales
frutas = ('banana', 'naranja', 'mango')
vegetales = ('tomate', 'zanahoria', 'lechuga')
productos_animales = ('leche', 'queso', 'yogur')

# Unir todas en food_stuff_tp
food_stuff_tp = frutas + vegetales + productos_animales
print("Food Stuff (tupla):", food_stuff_tp)

# Paso 3: Convertir la tupla a lista
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff (lista):", food_stuff_lt)

# Paso 4: Extraer el(los) elemento(s) del medio
longitud = len(food_stuff_lt)
if longitud % 2 == 0:
    items_medios = food_stuff_lt[longitud // 2 - 1: longitud // 2 + 1]
else:
    items_medios = [food_stuff_lt[longitud // 2]]
print("Elemento(s) del medio:", items_medios)

# Paso 5: Extraer los primeros y últimos tres elementos
primeros_tres = food_stuff_lt[:3]
ultimos_tres = food_stuff_lt[-3:]
print("Primeros tres:", primeros_tres)
print("Últimos tres:", ultimos_tres)

# Paso 6: Eliminar completamente la tupla food_stuff_tp
del food_stuff_tp
# print(food_stuff_tp)  # Esto causaría un error: NameError

# Paso 7: Verificar si un ítem existe en una tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("¿Estonia es un país nórdico?", 'Estonia' in nordic_countries)
print("¿Iceland es un país nórdico?", 'Iceland' in nordic_countries)
