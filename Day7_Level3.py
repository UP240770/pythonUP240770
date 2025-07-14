#1.-¿Cuál es más larga?
age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)

print("Lista original:", age)
print("Conjunto sin duplicados:", age_set)

print("Longitud de la lista:", len(age))
print("Longitud del set:", len(age_set))

if len(age) > len(age_set):
    print("La lista es más grande porque contiene elementos duplicados.")
elif len(age) < len(age_set):
    print("El set es más grande, pero esto no debería pasar en este caso.")
else:
    print("Ambos tienen la misma longitud.")

#2.-Diferencia entre string, list, tuple y set
"""En Python, una cadena (string) es un tipo de dato que representa texto y no puede modificarse una vez creado;
además, permite acceder a cada letra mediante índices. Una lista es una colección ordenada y modificable que puede
contener elementos repetidos, como números o palabras, y se accede a ellos por posición. Una tupla también es una
colección ordenada, pero no se puede cambiar después de su creación, lo que la hace útil para datos que deben
permanecer constantes. Por otro lado, un conjunto (set) es una colección no ordenada y sin duplicados,
ideal para almacenar elementos únicos y realizar operaciones como unión o intersección. La principal diferencia
entre estos tipos está en si se pueden modificar, si mantienen un orden y si permiten duplicados."""

#3.-Palabras unicas
frase = "I am a teacher and I love to inspire and teach people."

# Separar en palabras
palabras = frase.split()

# Convertir a conjunto para obtener solo únicas
palabras_unicas = set(palabras)

print("Palabras únicas:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))
