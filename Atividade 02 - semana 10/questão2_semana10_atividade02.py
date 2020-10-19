from operator import itemgetter
def preenche_lista(n):
    nascimento = []
    for i in range(n):
        ano = int(input('Digite o ano em que a pessoa nasceu: '))
        nascimento.append(ano)
    return nascimento

def main():
    resultado_nascimento = preenche_lista(1000)
    dicionario_nascimento = {}
    ranking = []
    for i in range(len(resultado_nascimento)):
        dicionario_nascimento[resultado_nascimento[i]] = resultado_nascimento.count(resultado_nascimento[i])
    print(dicionario_nascimento)
    ranking = sorted(dicionario_nascimento.items(), key = itemgetter(0))   
    for _, valor in enumerate(ranking):
        print(f'O ano {valor[0]}: apareceu {valor[1]} vezes.')
        
if __name__ == '__main__':
    main()
