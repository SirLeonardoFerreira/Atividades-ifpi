def main():
    dicionario_livros = {}
    codigo = 101
    condicao = True
    while True:
        if condicao == True:
            titulo = input('Digite o título do livro: ').strip()
            if titulo == '':
                condicao = False
            else:
                isbn = input('Digite o ISBN do livro: ').strip()
                autor = input('Digite o autor do livro: ').strip()
                preco = float(input('Digite o preço do livro: '))
                tupla_livro = (titulo, isbn, autor, preco)
                dicionario_livros[codigo] = tupla_livro
                codigo += 1
            
        else: break

    for cod in dicionario_livros:
        titulo_aux, isbn_aux, autor_aux, preco_aux = dicionario_livros[cod]
        print(f'Código: {cod}')
        print(f'Título: {titulo_aux}')
        print(f'ISBN: {isbn_aux}')
        print(f'Autor: {autor_aux}')
        print(f'Preço: {preco_aux:.2f}')

if __name__ == '__main__':
    main()
