def idade(dia_atuald, mes_atuald, ano_atuald, dia_nascimentos, mes_nascimentos, ano_nascimentos):
    if dia_atuald == dia_nascimentos and mes_atuald == mes_nascimentos:
        return ano_atuald - ano_nascimentos
    else:
        return (ano_atuald - ano_nascimentos) - 1


def main():
    dia_atual = int(input("Digite o dia de hoje: "))
    mes_atual = int(input("Digite o mês de hoje: "))
    ano_atual = int(input("Digite o ano de hoje: "))
    dia_nascimento = int(input("Digite o dia em que você nasceu: "))
    mes_nascimento = int(input("Digite o mês em que você nasceu: "))
    ano_nascimento = int(input("Digite o ano em que você nasceu: "))

    idade_atual = idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento)

    print(f'A sua idade é de {idade_atual} anos')

if __name__ == "__main__":
    main()

    
