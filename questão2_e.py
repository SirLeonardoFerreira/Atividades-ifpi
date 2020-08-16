altura = float(input("Digite a altura da sala: "))
comprimento = float(input("Digite o comprimento da sala: "))
largura = float(input("Digite a largura da sala: "))

area_do_piso_da_sala = largura * comprimento
volume_da_sala = largura * comprimento * altura
area_das_paredes_da_sala = (2 * altura * largura) + (2 * altura * comprimento)

print(f" A área do piso da sala é: {area_do_piso_da_sala:.2f} metros, o volume da sala é: {volume_da_sala:.2f} metros cúbicos e a área das paredes da sala é: {area_das_paredes_da_sala:.2f} metros")
