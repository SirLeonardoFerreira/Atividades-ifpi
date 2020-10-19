def media_notas(n_um, n_dois):
    return round((n_um + n_dois) / 2, 1)

def main():
    dicionario_alunos = {}
    condicao = True
    condicao_aux = True
    while True:
        if condicao == True:
            matricula = input().strip('Digite a matrícula do aluno: ')
            if matricula == '':
                condicao = False
            else:
                nome = input().strip('Digite o nome do aluno: ')
                nota_um = float(input('Digite a primeira nota do aluno: '))
                nota_dois = float(input('Digite a segunda nota do aluno: '))
                tupla_notas = (nome, nota_um, nota_dois)
                dicionario_alunos[matricula] = tupla_notas
            
        else: break

    while True:
        if condicao_aux == True:
            matricula_aux = input('Digite a matrícula do aluno a ser consultado: ').strip()
            if matricula_aux == '':
                condicao_aux = False

            else:
                nome_aux, nota_um_aux, nota_dois_aux = dicionario_alunos[matricula_aux]
                media = media_notas(nota_um_aux, nota_dois_aux)
                print(f'{nome_aux}: {media}')

        else: break
if __name__ == '__main__':
    main()
