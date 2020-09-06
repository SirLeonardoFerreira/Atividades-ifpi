def data(dia_primeiros, mes_primeiros, ano_primeiros, dia_segundos, mes_segundos, ano_segundos):
    if dia_primeiros > dia_segundos and mes_primeiros > mes_segundos and ano_primeiros > ano_segundos:
        return f'{dia_primeiros}/{mes_primeiros}/{ano_primeiros}'
    elif dia_primeiros > dia_segundos and mes_primeiros == mes_segundos and ano_primeiros == ano_segundos:
        return f'{dia_primeiros}/{mes_primeiros}/{ano_primeiros}'
    elif dia_primeiros == dia_segundos and mes_primeiros > mes_segundos and ano_primeiros == ano_segundos:
        return f'{dia_primeiros}/{mes_primeiros}/{ano_primeiros}'
    elif dia_primeiros == dia_segundos and mes_primeiros == mes_segundos and ano_primeiros > ano_segundos:
        return f'{dia_primeiros}/{mes_primeiros}/{ano_primeiros}'
    else:
        return f'{dia_segundos}/{mes_segundos}/{ano_segundos}'


def main():
    dia_primeiro = int(input())
    mes_primeiro = int(input())
    ano_primeiro = int(input())
    dia_segundo = int(input())
    mes_segundo = int(input())
    ano_segundo = int(input())

    maior_data = data(dia_primeiro, mes_primeiro, ano_primeiro, dia_segundo, mes_segundo, ano_segundo)

    print(maior_data)

if __name__ == "__main__":
    main()

    
