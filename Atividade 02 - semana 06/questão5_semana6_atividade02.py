def main():
    conceito_aluno = 'F'
    while True:
        nota_aluno = float(input("Digite a nota do aluno entre 0 e 10: "))
        if not conceito_aluno in 'A B C D E':
            if nota_aluno >= 8.5 and nota_aluno <= 10.0:
                conceito_aluno = 'A'
            elif nota_aluno >= 7.0 and nota_aluno <= 10.0:
                conceito_aluno = 'B'
            elif nota_aluno >= 5.0 and nota_aluno <= 10.0:
                conceito_aluno = 'C'
            elif nota_aluno >= 4.0 and nota_aluno <= 10.0:
                conceito_aluno = 'D'
            elif nota_aluno >= 0.0 and nota_aluno <= 10.0:
                conceito_aluno = 'E'
            elif nota_aluno < 0.0 or nota_aluno > 10.0:
                print("Nota inválida.")

        if conceito_aluno in 'A B C D E': break

    print(f'O conceito do aluno é {conceito_aluno}.')

if __name__ == '__main__':
    main()
    
