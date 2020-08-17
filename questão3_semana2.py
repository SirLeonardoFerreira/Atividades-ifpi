def tempo(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s

def main():
    valor_segundos = int(input("Digite a quantidade de segundos que o evento durou: "))
    h, m, s = tempo(valor_segundos)
    print(f'o evento durou {h} horas, {m} minutos e {s} segundos.')

if __name__ == '__main__':
    main()
