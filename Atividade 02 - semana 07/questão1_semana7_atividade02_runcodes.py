def main():
    numero = aux = int(input())
    produto = numero
    while True:
        if numero != 0:
            numero -= 1
            if numero != 0:
                produto *= numero

        elif produto == 0:
            produto = 1

        elif numero == 0: break

    print(f'{produto}')
        

if __name__ == '__main__':
    main()
