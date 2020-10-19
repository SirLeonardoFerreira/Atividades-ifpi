def preenche_dicionario(n):
    info = {}
    for i in range(n):
        nome = input('Digite o nome da pessoa: ').strip()
        idade = int(input('Digite a idade da pessoa: '))
        cpf = input('Digite o CPF da pessoa: ').strip()
        tupla_info = (nome, idade)
        info[cpf] = tupla_info
    return info

def main():
    dicionario_info = preenche_dicionario(20)
    menores_dezoito = {}
    for cod in dicionario_info:
        nome_aux, idade_aux = dicionario_info[cod]
        if idade_aux < 18:
            tupla_info_menores = (nome_aux, idade_aux)
            menores_dezoito[cod] = tupla_info_menores
    for codig in menores_dezoito:
        del dicionario_info[codig]

    print('========== MAIORES DE 18 ANOS ==========')    
    for codi in dicionario_info:
        nome_aux, idade_aux = dicionario_info[codi]
        print(f'{nome_aux};{idade_aux};{codi}')

    print('========== MENORES DE 18 ANOS ==========')
    for codig in menores_dezoito:
        nome_aux, idade_aux = menores_dezoito[codig]
        print(f'{nome_aux};{idade_aux};{codig}')
        
if __name__ == '__main__':
    main()
