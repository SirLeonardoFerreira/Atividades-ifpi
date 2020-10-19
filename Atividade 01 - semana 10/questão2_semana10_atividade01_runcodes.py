def preenche_dicionario(n):
    agenda = {}
    codigo = 0
    for ag in range(n):
        nome = input().strip()
        cidade = input().strip()
        estado = input().strip().upper()
        telefone = input().strip()
        tupla_agenda = (nome, cidade, estado, telefone)
        agenda[codigo] = tupla_agenda
        codigo += 1
    return agenda

def main():
    tamanho_dicionario = int(input())
    dicionario_agenda = preenche_dicionario(tamanho_dicionario)

    for cod in dicionario_agenda:
        nome_aux, cidade_aux, estado_aux, telefone_aux = dicionario_agenda[cod]
        cidade_estado = f'{cidade_aux}({estado_aux})'
        print(f'{nome_aux:25}{cidade_estado:30}{telefone_aux:30}')
if __name__ == '__main__':
    main()
