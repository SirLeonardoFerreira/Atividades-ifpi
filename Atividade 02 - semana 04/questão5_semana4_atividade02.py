def ordem(um, dois, tres):
    if um < dois < tres:
        return um, dois, tres
    elif um < tres < dois:
        return um, dois, tres
    elif dois < um < tres:
        return dois, um, tres
    elif dois < tres < um:
        return dois, tres, um
    elif tres < um < dois:
        return tres, um, dois
    elif tres < dois < um:
        return tres, dois, um

def main():
    numero_um = int(input("Digite o primeiro número: "))
    numero_dois = int(input("Digite o segundo número: "))
    numero_tres = int(input("Digite o terceiro número: "))

    um, dois, tres = ordem(numero_um, numero_dois, numero_tres)
    print(f'{um}')
    print(f'{dois}')
    print(f'{tres}')

if __name__ == '__main__':
    main()
