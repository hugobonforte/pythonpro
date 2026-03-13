meme_dict = {"CRINGE": "Significa algo excepcionalmente raro o embarazoso",
            "LOL": "Significa una respuesta común a algo gracioso",}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("Esa palabra no esta en el diccionario de memes")
            
