placar = 0
print('Calculadora do Amor')
print('<3 ' * 12)
casal = input("Por favor, Digite o nome de pessoas: ").lower()

for char in casal:

    if char in 'amor':
        placar += 10
if placar < 30:
    print(f'Seu placar de compatibilidade: {placar}')
    print("Esqueça esta pessoa!")
    
else:
    print(f'Seu placar de compatibilidade: {placar}')
    print('Vocês terão um relacionamento muito intenso! <3')
