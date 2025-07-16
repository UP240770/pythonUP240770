# Ejercicio 1: Extraer países que contienen "land"
from data.countries import countries

print("\n1. Países que contienen 'land':")
paises_con_land = [pais for pais in countries if 'land' in pais.lower()]
for pais in paises_con_land:
    print(f"- {pais}")

# Ejercicio 2: Invertir el orden de la lista de frutas
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []

for i in range(len(frutas)-1, -1, -1):
    frutas_invertidas.append(frutas[i])

print("\n2. Lista de frutas invertida:")
print(frutas_invertidas)

# Ejercicio 3: Análisis de datos de países
from data.countries_data import countries_data

# 3.1 Total de lenguajes únicos
lenguajes = set()
for pais in countries_data:
    for lenguaje in pais['languages']:
        lenguajes.add(lenguaje)

print(f"\n3.1 Total de lenguajes únicos: {len(lenguajes)}")

# 3.2 Los 10 lenguajes más hablados
conteo_lenguajes = {}
for pais in countries_data:
    for lenguaje in pais['languages']:
        conteo_lenguajes[lenguaje] = conteo_lenguajes.get(lenguaje, 0) + 1

top_lenguajes = sorted(conteo_lenguajes.items(), key=lambda x: x[1], reverse=True)[:10]

print("\n3.2 Top 10 lenguajes más hablados:")
for idx, (lenguaje, conteo) in enumerate(top_lenguajes, 1):
    print(f"{idx}. {lenguaje}: {conteo} países")

# 3.3 Los 10 países más poblados
paises_poblados = sorted(countries_data, 
                        key=lambda x: x['population'], 
                        reverse=True)[:10]

print("\n3.3 Top 10 países más poblados:")
for idx, pais in enumerate(paises_poblados, 1):
    nombre = pais['name']
    poblacion = f"{pais['population']:,}".replace(",", ".")
    print(f"{idx}. {nombre}: {poblacion} habitantes")