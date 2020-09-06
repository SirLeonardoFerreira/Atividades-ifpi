def idade(dia_atuald, mes_atuald, ano_atuald, dia_nascimentos, mes_nascimentos, ano_nascimentos):
    if dia_atuald >= dia_nascimentos and mes_atuald >= mes_nascimentos:
        return ano_atuald - ano_nascimentos
    else:
        return (ano_atuald - ano_nascimentos) - 1


def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    dia_nascimento = int(input())
    mes_nascimento = int(input())
    ano_nascimento = int(input())

    idade_atual = idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento)

    print(f'{idade_atual}')

if __name__ == "__main__":
    main()

    
