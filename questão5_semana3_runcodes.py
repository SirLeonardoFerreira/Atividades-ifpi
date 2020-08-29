def media(a, b, c):
    return (a + b + c) / 3
def ponto_extra(n):
    media_nova = n + 1 
    if media_nova > 10:
        media_final = 10
        return media_final
    else:
        return media_nova

def main():
    primeira_nota = int(input())
    segunda_nota = int(input())
    terceira_nota = int(input())

    media_notas = media(primeira_nota, segunda_nota, terceira_nota)

    if terceira_nota > 8:
        media_alunos = ponto_extra(media_notas)
        print(f'{media_alunos}')
    else:
        print(f'{media_notas}')


if __name__ == '__main__':
    main()
        
