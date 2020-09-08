def media_numeros(num):
    total_media = 0

    for n in range(num):
        numero = int(input("Digite um número: "))
        total_media += numero
    return total_media / 100

def main():
    valor_medio = media_numeros(100)
    print(f'O valor médio é: {valor_medio:.2f}')

    
if __name__ == '__main__':
    main()
