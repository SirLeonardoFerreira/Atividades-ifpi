textSpeakDictionary = {
    "rs" : "risos",
    "tbm" : "também",
    "vc" : "você",
    "pq" : "porquê",
    "blz" : "beleza"
    }

#obtém a frase pára tradução
sentence = input("Insira uma frase para traduzir: ").lower()

#divide a frase em uma lista de palavras
wordsToTranslate = sentence.split()

translatedSetence = ""

#passa por cada palavra da lista
for word in wordsToTranslate:
    #adiciona a palavra traduzida caso ela exista no dicionário
    if word in textSpeakDictionary:
        translatedSetence += textSpeakDictionary[word] + " "

    #mantém a palavra original caso não exista tradução
    else:
        translatedSetence += word + " "
        
#imprime a frase traduzida
print("==>")
print(translatedSetence)


