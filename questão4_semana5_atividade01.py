def sequencia_numeros(num, num_limite, num_multiplo):
    total_sequencia = ' '
    for n in range(num, num_limite,num_multiplo ):
        total_sequencia += str(n) + ', '
    return total_sequencia.strip(', ') +'.'

def main():
    print(sequencia_numeros(10, 1001, 10))

    
if __name__ == '__main__':
    main()
