from operator import itemgetter
def preenche_lista(n):
    nascimento = []
    for i in range(n):
        ano = int(input())
        nascimento.append(ano)
    return nascimento

def main():
    resultado_nascimento = preenche_lista(1000)
    dicionario_nascimento = {}
    ranking = []
    for i in range(len(resultado_nascimento)):
        dicionario_nascimento[resultado_nascimento[i]] = resultado_nascimento.count(resultado_nascimento[i])
    ranking = sorted(dicionario_nascimento.items(), key = itemgetter(0))   
    for _, valor in enumerate(ranking):
        print(f'{valor[0]}: {valor[1]}')
        
if __name__ == '__main__':
    main()
