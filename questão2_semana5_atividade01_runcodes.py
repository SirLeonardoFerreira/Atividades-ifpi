def par_impar(num):
    total_par = 0
    total_impar = 0

    for n in range(num):
        numero = int(input())
        if numero % 2 == 0:
            total_par += 1
        else:
            total_impar += 1
    return total_par, total_impar

def main():
    qtd_par, qtd_impar = par_impar(100)
    print(f'{qtd_par}')
    print(f'{qtd_impar}')

    
if __name__ == '__main__':
    main()
