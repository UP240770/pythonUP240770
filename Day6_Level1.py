# 1.- Crear una tupla vacía
tupla_vacia = ()
print("Tupla vacía:", tupla_vacia)

# 2.- Crear una tupla con nombres de hermanas y hermanos (ficticios si se desea)
hermanas = ('Aurora', 'Natalia', '')
hermanos = ('Alex', 'Adrian')
print("Hermanas:", hermanas)
print("Hermanos:", hermanos)

# 3.- Unir las tuplas de hermanos y hermanas y asignarla a 'hermanos_y_hermanas'
hermanos_y_hermanas = hermanas + hermanos
print("Hermanos y hermanas:", hermanos_y_hermanas)

# 4.- ¿Cuántos hermanos tienes?
print("Cantidad total de hermanos:", len(hermanos_y_hermanas))

# 5.- Modificar la tupla para agregar a mamá y papá (convertimos a lista, luego regresamos a tupla)
miembros_familia = list(hermanos_y_hermanas)  # convertimos a lista para modificar
miembros_familia.append('Paty')
miembros_familia.append('Felipe')
miembros_familia = tuple(miembros_familia)   # volvemos a convertir en tupla
print("Miembros de la familia:", miembros_familia)
