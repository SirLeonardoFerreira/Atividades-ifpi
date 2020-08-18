def tempo(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return h, m, s

def main():
    valor_segundos = int(input())
    h, m, s = tempo(valor_segundos)
    print(f'{h}:{m}:{s}')
if __name__ == '__main__':
    main()
