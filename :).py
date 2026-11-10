None
#Almacenamiento
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO ": "ponerse agresivo/enojado"
            }
#solucitud
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

#prosesar solucitud y debolucion 
if word in meme_dict.keys():
   print(meme_dict[word])
else:
    print("Lo siento, esa palabra no está en el diccionario.")
