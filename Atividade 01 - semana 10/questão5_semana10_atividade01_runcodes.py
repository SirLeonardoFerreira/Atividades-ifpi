def media_notas(n_um, n_dois):
    return round((n_um + n_dois) / 2, 1)

def main():
    dicionario_alunos = {}
    condicao = True
    condicao_aux = True
    while True:
        if condicao == True:
            matricula = input().strip()
            if matricula == '':
                condicao = False
            else:
                nome = input().strip()
                nota_um = float(input())
                nota_dois = float(input())
                tupla_notas = (nome, nota_um, nota_dois)
                dicionario_alunos[matricula] = tupla_notas
            
        else: break

    while True:
        if condicao_aux == True:
            matricula_aux = input().strip()
            if matricula_aux == '':
                condicao_aux = False

            else:
                nome_aux, nota_um_aux, nota_dois_aux = dicionario_alunos[matricula_aux]
                media = media_notas(nota_um_aux, nota_dois_aux)
                print(f'{nome_aux}: {media}')

        else: break
if __name__ == '__main__':
    main()
