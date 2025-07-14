# Paso 1: Crear un diccionario vacío llamado dog
dog = {}

# Paso 2: Agregar claves y valores
dog['name'] = 'Firulais'
dog['color'] = 'marrón'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# Paso 3: Crear el diccionario student
student = {
    'first_name': 'Mira',
    'last_name': 'Rumi',
    'gender': 'Non-binary',
    'age':18,
    'marital_status': 'single',
    'skills': ['Python', 'HTML'],
    'country': 'Canada',
    'city': 'Toroto',
    'address': 'Calle  123'
}

# Paso 4: Obtener la longitud del diccionario student
print("Longitud del diccionario student:", len(student))

# Paso 5: Obtener el valor de skills y verificar su tipo
skills = student['skills']
print("Habilidades:", skills)
print("Tipo de datos de 'skills':", type(skills))

# Paso 6: Agregar habilidades
student['skills'].append('CSS')
student['skills'].append('JavaScript')

# Paso 7: Obtener las claves como lista
keys = list(student.keys())
print("Claves del diccionario:", keys)

# Paso 8: Obtener los valores como lista
values = list(student.values())
print("Valores del diccionario:", values)

# Paso 9: Convertir el diccionario en una lista de tuplas
items = list(student.items())
print("Diccionario como lista de tuplas:", items)

# Paso 10: Eliminar un ítem (por ejemplo, 'marital_status')
student.pop('marital_status')

# Paso 11: Eliminar el diccionario dog
del dog

# Mostrar diccionario student final
print("Diccionario student final:", student)
