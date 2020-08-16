def segundos(hr, minu, segun):
    return (((hr * 60) + minu ) * 60) + segun 


def main():
    hora = int(input("Digite quantos horas são: "))
    minuto = int(input("Digite quantos minutos são: "))
    segundo = int(input("Digite quantos segundos são: "))
    segundo_totais = segundos(hora, minuto, segundo)
    print(f"Desde a última noite, passaram {segundo_totais:.2f} segundos")

if __name__ == '__main__':
    main()
