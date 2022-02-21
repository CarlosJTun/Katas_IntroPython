# Texto a analizar:

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""


# Normaliza primero el texto eliminando las mayusculas y ademas separa cada palabra

contenido = text.lower().split()
texto_normalizado = []


# Verifica si la palabra contiene puntos o comas y las elimina

for palabra in contenido:
    if palabra.endswith(",") or palabra.endswith("."):
        palabra = palabra.replace(",","")
        palabra = palabra.replace(".","")
    texto_normalizado.append(palabra)

print(texto_normalizado)

# Dividimos el texto en palabras (lo dejamos en minúsculas para normalizar el contenido):


# Definimos las palabras clave:

keywords = ['average', 'temperature', 'distance']


for keyword in keywords:
    if keyword in texto_normalizado:
        PosKW = texto_normalizado.find(keyword)   #Listas no tienen este atributo, lo que se usa es .index()
        print(f"Existe {PosKW}")

    else:
        print("Nanai")

