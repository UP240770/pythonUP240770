'Day 2: 30 Days of python progamming'
# Información personal
first_name = "Noé Ezequiel"
last_name = "Estrada Ramírez"
full_name = first_name + " " + last_name
country = "México"
city = "Aguascalientes"
age = 18
year = 2006

# Variables booleanas
is_married = False
is_true = True
is_light_on = False

# Multiples variables
variable_a, variable_b, variable_c = 10, "hola", 3.14

'''Level 2'''
# Revisar los tipos de datos
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(variable_a))
print(type(variable_b))
print(type(variable_c))

# Longitud del primer nombre
print("Longitud del primer nombre:", len(first_name))

# Comparar longitud del primer y último nombre
print("¿Primer nombre más largo que el apellido?", len(first_name) > len(last_name))
print("¿Apellido más largo que el primer nombre?", len(last_name) > len(first_name))
print("¿Tienen la misma longitud?", len(first_name) == len(last_name))

# Operaciones con números
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
residuo = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Suma:", total)
print("Resta:", diff)
print("Multiplicación:", product)
print("División:", division)
print("Módulo:", residuo)
print("Exponenciación:", exp)
print("División entera:", floor_division)

#Claculo del radio
area_of_circle = 3.1416 * 30 ** 2
circum_of_circle = 2 * 3.1416 * 30
print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

#Datos dados por el usuario 
radio_dado = float(input("Introduce el radio de un círculo: "))
area_calculada = 3.1416 * radio_dado ** 2
print ('El area del cirulo con el radio ', radio_dado, ' es: ', area_calculada)

# Datos personales ingresados por el usuario
user_first_name = input("Ingresa tu primer nombre: ")
user_last_name = input("Ingresa tu apellido: ")
user_country = input("Ingresa tu país: ")
user_age = input("Ingresa tu edad: ")

# Palabras clave en Python
help('keywords')