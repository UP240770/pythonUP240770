# Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1.- Encontrar la longitud del conjunto it_companies
print("Longitud de it_companies:", len(it_companies))

# 2.- Agregar 'Twitter' a it_companies
it_companies.add('Twitter')
print("Después de agregar Twitter:", it_companies)

# 3.- Insertar varias compañías al mismo tiempo
it_companies.update(['Tesla', 'Samsung', 'Intel'])
print("Después de agregar múltiples compañías:", it_companies)

# 4.- Eliminar una compañía del conjunto
it_companies.remove('Samsung')
print("Después de eliminar Samsung:", it_companies)

# 5.- Diferencia entre remove y discard:
# - remove(): lanza un error si el elemento no existe
# - discard(): no lanza error si el elemento no existe
