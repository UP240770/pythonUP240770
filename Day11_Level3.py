#1. Función para verificar si un número es primo
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

#2. Función para verificar si todos los elementos de una lista son únicos
def all_unique(items):
    """Check if all items in a list are unique."""
    return len(items) == len(set(items))

#3. Función para verificar si todos los elementos son del mismo tipo
def same_type(items):
    """Check if all items in a list are of the same type."""
    if not items:
        return True
    first_type = type(items[0])
    return all(isinstance(item, first_type) for item in items)

#4. Función para verificar si una variable es un identificador válido en Python
def is_valid_variable(name):
    """Check if a string is a valid Python variable name."""
    if not name:
        return False
    if not (name[0].isalpha() or name[0] == '_'):
        return False
    for char in name[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    return True

#5. Funciones para trabajar con datos de países 
#-Función para los idiomas más hablados
from countries_data import countries

def most_spoken_languages(n=10):
    """Return the n most spoken languages in descending order."""
    language_count = {}
    
    for country in countries:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + country['population']
    
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return [(lang, count) for lang, count in sorted_languages[:n]]

#-Función para los países más poblados

from countries_data import countries

def most_populated_countries(n=10):
    """Return the n most populated countries in descending order."""
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:n]]
