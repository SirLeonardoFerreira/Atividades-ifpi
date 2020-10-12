def celsius(c):
    return  (c - 32) * (5/9)

def fahrenheit(f):
    return (f * (9/5)) + 32 


def main():
    temp_um = float(input("Digite a primeira temperatura: "))
    escala_um =  input("Digite a escala da temperatura: ").upper()[0]
    temp_dois = float(input("Digite a segunda temperatura: "))
    escala_dois =  input("Digite a escala da temperatura: ").upper()[0]
    if (escala_um in 'C' and escala_dois in 'C') or (escala_um in 'F' and escala_dois in 'F'):
        if temp_um > temp_dois:
            temperatura = (temp_um, escala_um)
        else:
            temperatura = (temp_dois, escala_dois)

    else:
        if escala_um in 'F':
            temp_atual = celsius(temp_um)
            if temp_atual > temp_dois:
                temperatura = (temp_um, escala_um)
            else:
                temperatura = (temp_dois, escala_dois)
        elif escala_um in 'C':
            temp_atual = fahrenheit(temp_um)
            if temp_atual > temp_dois:
                temperatura = (temp_um, escala_um)
            else:
                temperatura = (temp_dois, escala_dois)

    print(temperatura)

if __name__ == '__main__':
    main()
