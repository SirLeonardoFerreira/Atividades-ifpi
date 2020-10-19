agenda = {}
def incluirNovoNome(nome, telefone):
    lista_telefone = []
    if nome in agenda:
        print('Nome já existe na agenda.')

    else:
        lista_telefone.append(telefone)
        agenda[nome] = lista_telefone
    return agenda

def consultarTelefone(codigo):
    telefone = agenda[codigo]
    return telefone

def incluirTelefone():
    aux = input('Digite o nome da pessoa que deseja adicionar mais um telefone: ').strip()
    telefone = input('Digite o telefone a ser inclído: ').strip()
    if aux in agenda:
        agenda[aux].append(telefone)
        
    else:
        nome = aux
        aux = input()[0].upper()
        if aux == 'S':
            incluirNovoNome(nome, telefone)

def excluirTelefone():
    nome = input('Digite o nome da pessoa que deseja excluir o telefone: ').strip()
    telefone = input('Digite o telefone que vai ser excluído: ').strip()
    if nome in agenda:
        lista_telefone = consultarTelefone(nome)
        for i in range(len(lista_telefone)):
            if lista_telefone[i] == telefone:
                indice_telefone = lista_telefone.index(lista_telefone[i])
        del agenda[nome][indice_telefone]
        if agenda[nome] == []:
            del agenda[nome]

def excluirNome():
    nome = input('Digite o nome da pessoa que deseja excluir: ').strip()
    if nome in agenda:
        del agenda[nome]
    else:
        print(f'{nome} não está na agenda.')

def listarAgenda():
    qtd = 0
    for codigo in agenda:
        telefone = consultarTelefone(codigo)
        qtd += 1
        print(f'Nome: {codigo}')
        print(f'  Telefone(s):')
        for i in range(len(telefone)):
            print(f'    {i+1}. {telefone[i]}')

    if qtd == 0:
        print('<<< Nenhuma pessoa para mostrar >>>')

def menu():
    while True:
        print('1 - Incluir nova pessoa')
        print('2 - Incluir novo telefone')
        print('3 - Excluir Telefone')
        print('4 - Excluir pessoa')
        print('5 - Listar agenda')
        print('0 - Fim do programa')
        print('=' * 30)
        opcao = int(input("Digite o que deseja: "))
        if opcao in (1, 2, 3, 4, 5, 6, 0):
            return opcao
        else:
            print('Opção inválida')

def main():
    while True:
        op = menu()
        if op == 1:
            nome = input('Digite o nome que deseja adicionar: ').strip()
            telefone = input('Digite o telefone da pessoa: ').strip()
            incluirNovoNome(nome, telefone)
        elif op == 2:
            incluirTelefone()
            
        elif op == 3:
            excluirTelefone()

        elif op == 4:
            excluirNome()
            
        elif op == 5:
            listarAgenda()
        elif op == 0:
            break
        else:
            pass
