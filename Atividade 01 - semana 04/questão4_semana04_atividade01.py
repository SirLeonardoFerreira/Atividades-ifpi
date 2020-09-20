def media(numero_ums, numero_doiss, numero_tress, numero_quatros, numero_cincos):
    return (numero_ums + numero_doiss + numero_tress + numero_quatros + numero_cincos) / 5


def main():
    
    numero_um = int(input("Digite o primeiro numero: "))
    numero_dois = int(input("Digite o segundo numero: "))
    numero_tres = int(input("Digite o terceiro numero: "))
    numero_quatro = int(input("Digite o quarto numero: "))
    numero_cinco = int(input("Digite o quinto numero: "))

    media_numero = media(numero_um, numero_dois, numero_tres, numero_quatro, numero_cinco)
    print(f'{media_numero:.2f}')
    if numero_um > media_numero:
       print(f'{numero_um:.2f}')
       if numero_dois > media_numero:
           print(f'{numero_dois:.2f}')
           if numero_tres > media_numero:
               print(f'{numero_tres:.2f}')
               if numero_quatro > media_numero:
                   print(f'{numero_quatro:.2f}')
                   if numero_cinco > media_numero:
                       print(f'{numero_cinco:.2f}')
    elif numero_dois > media_numero:
        print(f'{numero_dois:.2f}')
        if numero_tres > media_numero:
               print(f'{numero_tres:.2f}')
               if numero_quatro > media_numero:
                   print(f'{numero_quatro:.2f}')
                   if numero_cinco > media_numero:
                       print(f'{numero_cinco:.2f}')
    elif numero_tres > media_numero:
        print(f'{numero_tres:.2f}')
        if numero_quatro > media_numero:
                   print(f'{numero_quatro:.2f}')
                   if numero_cinco > media_numero:
                       print(f'{numero_cinco:.2f}')
    elif numero_quatro > media_numero:
                   print(f'{numero_quatro:.2f}')
                   if numero_cinco > media_numero:
                       print(f'{numero_cinco:.2f}')
    elif numero_cinco > media_numero:
                       print(f'{numero_cinco:.2f}')

if __name__ == '__main__':
    main()

