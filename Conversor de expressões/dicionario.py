textSpeakDictionary = {
    "rs" : "risos",
    "tbm" : "também"
    }
#imprime o dicionário inteiro
print("Dicionário =", textSpeakDictionary)

#imprime apenas o conteúdo relacionado á chave 'rs'
print( "\nrs =", textSpeakDictionary["rs"])

#texto que pede a entrada do usuário
key = input("\nO o que você gostaria de converter? : ")
print(key , "=" , textSpeakDictionary[key])
