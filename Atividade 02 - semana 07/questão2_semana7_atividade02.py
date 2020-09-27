def sequencia_numeros(numero):
    ultimo = 0
    sequencia = ' '
    for num in range(numero - 1):
        if ultimo == 0:
            sequencia += str(ultimo) + ', '
            penultimo = ultimo
            ultimo += 1
            if penultimo == 0:
                sequencia += str(ultimo) + ', '

        else:
            ultimo += penultimo
            sequencia += str(ultimo) + ', '
            penultimo = ultimo - penultimo
    return sequencia.strip(', ') +'.'
def main():
    numero = int(input("Digite um número maior ou igual a 2: "))
    resultado_sequencia = sequencia_numeros(numero)
    print(resultado_sequencia)

if __name__ == '__main__':
    main()
