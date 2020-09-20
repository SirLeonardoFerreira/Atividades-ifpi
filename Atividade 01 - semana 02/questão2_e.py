def piso_sala(lar, com):
    return lar * com

def volume_sala(lar, com, altu):
    return lar * com * altu

def parede_sala(lar, com, altu):
    return (2 * altu * lar) + (2 * altu * com)

def main():
    altura = float(input("Digite a altura da sala: "))
    comprimento = float(input("Digite o comprimento da sala: "))
    largura = float(input("Digite a largura da sala: "))

    area_do_piso_da_sala = piso_sala(largura, comprimento)
    volume_da_sala = volume_sala(largura, comprimento, altura)
    area_das_paredes_da_sala = parede_sala(largura, comprimento, altura)

    print(f" A área do piso da sala é: {area_do_piso_da_sala:.2f} metros, o volume da sala é: {volume_da_sala:.2f} metros cúbicos e a área das paredes da sala é: {area_das_paredes_da_sala:.2f} metros")

if __name__ == '__main__':
    main()

