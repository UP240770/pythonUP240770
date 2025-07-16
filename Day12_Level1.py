# 1.- Función que genera un ID de usuario aleatorio de 6 caracteres
import string
import random

def random_user_id():
    caracteres = string.ascii_letters + string.digits
    id_generado = ''.join(random.choices(caracteres, k=6))
    return id_generado

# Ejemplo:
# print(random_user_id()) → '1ee33d'

# 2.- Función que genera múltiples IDs según número de caracteres y número de IDs indicados por el usuario

def user_id_gen_by_user():
    caracteres = string.ascii_letters + string.digits
    num_caracteres = int(input("Ingrese la longitud de los IDs: "))
    num_ids = int(input("Ingrese cuántos IDs generar: "))

    for _ in range(num_ids):
        id_generado = ''.join(random.choices(caracteres, k=num_caracteres))
        print(id_generado)

# Ejemplo:
# print(user_id_gen_by_user())
# Entrada del usuario:
# 5
# 5
# Salida esperada:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf

# 3.- Función que genera un color RGB aleatorio

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# Ejemplo:
# print(rgb_color_gen()) → 'rgb(125,244,255)'
