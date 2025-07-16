# Paso 1: Asignar calificaciones según el puntaje
Puntaje = int(input("Ingresa tu puntaje (0-100): "))

if 80 <= Puntaje <= 100:
    print("Grado: A")
elif 70 <= Puntaje :
    print("Grado: B")
elif 60 <= Puntaje :
    print("Grado: C")
elif 50 <= Puntaje :
    print("Grado: D")
elif 0 <= Puntaje :
    print("Grado: F")
else:
    print("Puntaje invalido")

# Paso 2: Determinar la estación del año según el mes
mes = input("Ingresa un mes: ").capitalize()

if mes in ['Septiembre', 'Octubre', 'Noviembre']:
    print("Estación: Otoño")
elif mes in ['Diciembre', 'Enero', 'Febrero']:
    print("Estación: Invierno")
elif mes in ['Marzo', 'Abril', 'Mayo']:
    print("Estación: Primavera")
elif mes in ['Junio', 'Julio', 'Agosto']:
    print("Estación: Verano")
else:
    print("Mes invalido")

# Paso 3: Verificar y agregar fruta a la lista
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta_nueva = input("Ingresa un fruta: ").lower()

if fruta_nueva in fruits:
    print("La fruta ya existe en la lista")
else:
    fruits.append(fruta_nueva)
    print("Fruta agregada. Lista actualizada:", fruits)
