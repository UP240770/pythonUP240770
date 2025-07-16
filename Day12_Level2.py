#1.-Genera una lista con n colores hexadecimales aleatorios.
import random

def list_of_hexa_colors(n):
    colores_hex = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores_hex.append(color)
    return colores_hex

# Ejemplo:
# print(list_of_hexa_colors(3)) → ['#a3e12f', '#03ed55', '#eb3d2b']

#2.-Genera una lista con n colores RGB aleatorios.
def list_of_rgb_colors(n):
    colores_rgb = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores_rgb.append(f"rgb({r},{g},{b})")
    return colores_rgb

# Ejemplo:
# print(list_of_rgb_colors(2)) → ['rgb(34,200,45)', 'rgb(101,88,240)']

#3.-Permite generar colores en formato hexa o rgb, según lo que se indique en el parámetro tipo.
def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo inválido. Usa 'hexa' o 'rgb'."

# Ejemplos:
# print(generate_colors('hexa', 3)) → ['#a3e12f','#03ed55','#eb3d2b']
# print(generate_colors('rgb', 2)) → ['rgb(5, 55, 175)', 'rgb(50, 105, 100)']
