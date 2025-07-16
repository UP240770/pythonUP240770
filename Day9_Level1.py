# 1.- Verificar si el usuario puede aprender a conducir
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Tienes la edad para manejar.")
else:
    print(f"Necesitas {18 - edad} años más para aprender a manejar.")

# 2.- Comparar edades entre tú y el usuario
mi_edad = 25
tu_edad = int(input("Ingresa tu edad: "))

if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print("Eres un año mayor a mi.")
    else:
        print(f"Tienes {diferencia} años más que yo.")
elif tu_edad < mi_edad:
    diferencia = mi_edad - tu_edad
    if diferencia == 1:
        print("Soy un año mayor qu tu.")
    else:
        print(f"Soy {diferencia} años másgrande que tu.")
else:
    print("Tenemos la misma edad.")

# 3.- Comparar dos números
a = float(input("Ingresa el primer número: "))
b = float(input("Ingrea el segundo número: "))

if a > b:
    print(f"{a} es más grande que {b}")
elif a < b:
    print(f"{a} es más pequeño que {b}")
else:
    print(f"{a} es igual a {b}")
