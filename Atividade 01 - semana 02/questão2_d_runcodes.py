def segundos(hr, minu, segun):
    return (((hr * 60) + minu ) * 60) + segun 


def main():
    hora = int(input())
    minuto = int(input())
    segundo = int(input())
    segundo_totais = segundos(hora, minuto, segundo)
    print(f"{segundo_totais:.2f}")

if __name__ == '__main__':
    main()
