#1.-Toma una lista como parámetro y devuelve una nueva lista con los elementos desordenados (aleatoriamente):
import random

def shuffle_list(lista):
    lista_mezclada = lista.copy()
    random.shuffle(lista_mezclada)
    return lista_mezclada

# Ejemplo:
# print(shuffle_list([1, 2, 3, 4, 5])) → [3, 5, 1, 4, 2] (puede variar)

#2.-Genera una lista con 7 números aleatorios únicos entre 0 y 9:
def unique_random_numbers():
    return random.sample(range(10), 7)  # sample asegura que no se repitan

# Ejemplo:
# print(unique_random_numbers()) → [3, 0, 7, 1, 9, 5, 2] (puede variar)
