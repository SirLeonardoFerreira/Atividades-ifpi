def numero_maior(num):
    num_maior = 0

    for n in range(num):
        numero = int(input())
        if num_maior < numero:
            num_maior = numero
    return num_maior

def main():
    valor_maior = numero_maior(100)
    print(f'{valor_maior}')

    
if __name__ == '__main__':
    main()
