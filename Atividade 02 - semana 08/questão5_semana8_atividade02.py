def ler_nomes(num):
    lista_nomes = []
    lista_altura = []
    lista_idade = []
    for i in range(num):
        nomes = input("Digite os nomes dos alunos: ")
        lista_nomes.append(nomes)
        idade = int(input("Digite a idade dos alunos: "))
        lista_idade.append(idade)
        numero = float(input("Digite a altura dos alunos: "))
        lista_altura.append(numero)
    return lista_nomes, lista_idade, lista_altura

def media_altura(num):
    media = sum(num) / len(num)
    return round(media, 2)

def main():
    resultado_ler_nomes, resultado_ler_idade, resultado_ler_altura = ler_nomes(30)
    resultado_media_altura = media_altura(resultado_ler_altura)
    aux_posicao = 0
    print(f'MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    for idade in resultado_ler_idade: 
        if idade > 13:
            indice_idade = resultado_ler_idade.index(idade, aux_posicao)
            if resultado_ler_altura[indice_idade] < resultado_media_altura:
                print(f'{resultado_ler_nomes[indice_idade]}')
        aux_posicao += 1
        
if __name__ == '__main__':
    main()
