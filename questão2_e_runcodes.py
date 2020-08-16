def piso_sala(lar, com):
    return lar * com

def volume_sala(lar, com, altu):
    return lar * com * altu

def parede_sala(lar, com, altu):
    return (2 * altu * lar) + (2 * altu * com)

def main():
    altura = float(input())
    comprimento = float(input())
    largura = float(input())

    area_do_piso_da_sala = piso_sala(largura, comprimento)
    volume_da_sala = volume_sala(largura, comprimento, altura)
    area_das_paredes_da_sala = parede_sala(largura, comprimento, altura)

    print(f"{area_do_piso_da_sala:.2f} metros, {volume_da_sala:.2f} {area_das_paredes_da_sala:.2f}")

if __name__ == '__main__':
    main()

