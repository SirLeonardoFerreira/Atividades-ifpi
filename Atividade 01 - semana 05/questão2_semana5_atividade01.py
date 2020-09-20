def par_impar(num):
    total_par = 0
    total_impar = 0

    for n in range(num):
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            total_par += 1
        else:
            total_impar += 1
    return total_par, total_impar

def main():
    qtd_par, qtd_impar = par_impar(100)
    print(f'Tem {qtd_par} números pares')
    print(f'Tem {qtd_impar} números ímpares')

    
if __name__ == '__main__':
    main()
