def celsius(c):
    return  (c - 32) * (5/9)

def fahrenheit(f):
    return (f * (9/5)) + 32 

def calculo_temperatura(tum, tdois):
    return round(tum + tdois, 4)

def main():
    temp_um = float(input("Digite a primeira temperatura: "))
    escala_um =  input("Digite a escala da temperatura: ").upper()[0]
    temp_dois = float(input("Digite a segunda temperatura: "))
    escala_dois =  input("Digite a escala da temperatura: ").upper()[0]
    if (escala_um in 'C' and escala_dois in 'C') or (escala_um in 'F' and escala_dois in 'F'):
        temperatura_total = (calculo_temperatura(temp_um, temp_dois), escala_um)

    else:
        if escala_um in 'F':
            temp_atual = celsius(temp_um)
            temperatura_total = (calculo_temperatura(temp_atual, temp_dois), escala_dois)
                
        elif escala_um in 'C':
            temp_atual = fahrenheit(temp_um)        
            temperatura_total = (calculo_temperatura(temp_atual, temp_dois), escala_dois)

    print(temperatura_total)

if __name__ == '__main__':
    main()
