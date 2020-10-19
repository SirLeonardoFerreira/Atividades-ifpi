def displayMenu():
    print("trdtr de exprss")
    print("=" * 13)
    print("Menu:")
    print(" c = converter uma frase")
    print(" p = imprimir dicionário")
    print(" a = adicionar uma palavra")
    print(" d = remover uma palavra")
    print(" q = sair")

#----------------------------------------------
def convertSetence():
    sentence = input("Insira uma frase para traduzir: ").lower()
    translatedSetence = ""

    #remove a pontuação da frase
    for char in '?!.,':
        sentence = sentence.replace(char, '')
        
    #divide a frase em uma lista de palavras
    listOfWords = sentence.split()

    for word in listOfWords:
        #adiciona a palavra traduzida se ela existir no dicionário
        if word in textSpeakDictionary:
            translatedSetence += textSpeakDictionary[word] + " "

        #mantém a palavra original caso não exista tradução
        else:
            translatedSetence += word + " "
    #imprime a frase traduzida
    print("==>")
    print(translatedSetence)

#--------------------------------------------------------------------
def addDictionaryItem():
    txtToAdd = input("Insira a expressão a ser adicionada ao dicionário: ")
    meaning = input("O que ela significa?: ")
    #adiciona a nova tradução ao dicionário
    if txtToAdd not in textSpeakDictionary:
        textSpeakDictionary[txtToAdd] = meaning
    else:
        print("A expressão já existe no dicionário!")

#---------------------------------------------------------------------
def deleteDictionaryItem():
    txtToDelete = input("Insira a expressão a ser removida ao dicionário: ")
    #remove a tradução do dicionário
    if txtToDelete not in textSpeakDictionary:
        print("A expressão não existe no dicionário!")
    else:
        del textSpeakDictionary[txtToDelete]

#-----------------------------------------------------------------------
# o programa principal começa aqui
#-----------------------------------------------------------------------

textSpeakDictionary = {
    "rs" : "risos",
    "tbm" : "também",
    "vc" : "você",
    "pq" : "porquê"
    }

running = True
displayMenu()

#repete até que o usuário digite 'q' para sair
while running == True:
    menuChoice = input(">_").lower()

    #c para converter
    if menuChoice == 'c':
        convertSetence()

    #p para imprimir
    elif menuChoice == 'p':
        print(textSpeakDictionary)

    #a para adicionar
    elif menuChoice == 'a':
        addDictionaryItem()

    #d para remover
    elif menuChoice == 'd':
        deleteDictionaryItem()
    #q para sair
    elif menuChoice == 'q':
        running = False

    else:
        print("Escolha inválida!")


