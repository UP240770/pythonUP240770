# 1.- Declarar una lista vacía
lista_vacia = []

# 2.- Declarar una lista con más de 5 elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'morado']

# 3.- Obtener la longitud de la lista
print("Longitud de la lista de colores:", len(colores))

# 4.- Obtener el primer, el del medio y el último elemento de la lista
primero = colores[0]
medio = colores[len(colores) // 2]
ultimo = colores[-1]
print("Primero:", primero, " | Medio:", medio, " | Último:", ultimo)

# 5.- Declarar lista con tipos de datos mezclados
# Pregunta: ¿Cuál es tu nombre, edad, estatura, estado civil y dirección?
mixed_data_types = ['Noé', 18, 1.70, 'Soltero', 'Aguascalientes, México']
print("Datos personales:", mixed_data_types)

# 6.- Declarar la lista it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7.- Imprimir la lista
print("Empresas tecnológicas:", it_companies)

# 8.- Imprimir número de empresas
print("Número de empresas:", len(it_companies))

# 9.- Imprimir primera, media y última empresa
primera_empresa = it_companies[0]
media_empresa = it_companies[len(it_companies) // 2]
ultima_empresa = it_companies[-1]
print("Primera:", primera_empresa, " | Media:", media_empresa, " | Última:", ultima_empresa)

# 10.- Modificar una empresa
it_companies[1] = 'Alphabet'
print("Empresas actualizadas:", it_companies)

# 11.- Agregar una empresa
it_companies.append('Tesla')
print("Agregada Tesla:", it_companies)

# 12.- Insertar una empresa en medio
it_companies.insert(len(it_companies)//2, 'Spotify')
print("Insertada en el medio:", it_companies)

# 13.- Cambiar un nombre a mayúsculas (excluyendo IBM)
for i in range(len(it_companies)):
    if it_companies[i] != 'IBM':
        it_companies[i] = it_companies[i].upper()
        break
print("Con mayúsculas:", it_companies)

# 14.- Unir la lista con '#; '
empresas_str = '#; '.join(it_companies)
print("Empresas unidas con '#;':", empresas_str)

# 15.- Verificar si una empresa existe
empresa_busqueda = 'GOOGLE'
existe = empresa_busqueda in it_companies
print(f"¿Existe {empresa_busqueda}?:", existe)

# 16.- Ordenar la lista
it_companies.sort()
print("Empresas ordenadas:", it_companies)

# 17.- Invertir la lista
it_companies.reverse()
print("Empresas en orden inverso:", it_companies)

# 18.- Extraer las primeras 3
primeras_tres = it_companies[:3]
print("Primeras tres empresas:", primeras_tres)

# 19.- Extraer las últimas 3
ultimas_tres = it_companies[-3:]
print("Últimas tres empresas:", ultimas_tres)

# 20.- Extraer la(s) empresa(s) del medio
medio_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    empresas_medias = it_companies[medio_index-1:medio_index+1]
else:
    empresas_medias = [it_companies[medio_index]]
print("Empresa(s) del medio:", empresas_medias)

# 21.- Eliminar la primera empresa
del it_companies[0]
print("Eliminada la primera empresa:", it_companies)

# 22.- Eliminar la(s) empresa(s) del medio
medio_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[medio_index-1:medio_index+1]
else:
    del it_companies[medio_index]
print("Eliminada empresa(s) del medio:", it_companies)

# 23.- Eliminar la última empresa
it_companies.pop()
print("Eliminada última empresa:", it_companies)

# 24.- Eliminar todos los elementos
it_companies.clear()
print("Lista vacía:", it_companies)

# 25.- Destruir la lista completamente
del it_companies
# print(it_companies)  # Esto daría un error: NameError

# 26.- Unir las siguientes listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
tecnologias = front_end + back_end
print("Listas unidas:", tecnologias)

# 27.- Copiar la lista unida a full_stack y agregar Python y SQL después de Redux
full_stack = tecnologias.copy()
indice_redux = full_stack.index('Redux')
full_stack.insert(indice_redux + 1, 'Python')
full_stack.insert(indice_redux + 2, 'SQL')
print("Full Stack final:", full_stack)
