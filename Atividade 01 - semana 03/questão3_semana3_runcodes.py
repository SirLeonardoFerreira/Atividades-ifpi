def sinal_transito(sinal):
    if sinal.upper() == 'V':
        return 'Siga'
    elif sinal.upper() == 'A':
        return 'Atenção'
    else:
        return 'Pare'

def main():
    cor_sinal = input()
    mensagem = sinal_transito(cor_sinal)

    print(f'{mensagem}')

if __name__ == '__main__':
    main()
        
