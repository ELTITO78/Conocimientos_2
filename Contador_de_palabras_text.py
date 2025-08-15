#programa para contar palabras en un archivo de texto
archivo = input("Introduce la ruta del archivo de texto: ")
try:
    with open(archivo, 'r', encoding='utf-8') as file:
        texto = file.read()
except FileNotFoundError:
    print("El archivo no fue encontrado")
    exit()

#Seperar en palabras
import re
palabras = re.findall(r"\w+",texto.lower())
total_palabras = len(palabras)
print(f"Total de palabras: {total_palabras}")

#Contar frecuencias
from collections import Counter
contador = Counter(palabras)
mas_comunes = contador.most_common(10)
print("\nLas 10 palabras más frecuentes:")
for palabra, frecuencia in mas_comunes:
 print(f"{palabra}: {frecuencia}")
