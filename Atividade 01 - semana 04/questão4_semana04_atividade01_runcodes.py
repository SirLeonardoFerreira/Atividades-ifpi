def media(numero_ums, numero_doiss, numero_tress, numero_quatros, numero_cincos):
    return (numero_ums + numero_doiss + numero_tress + numero_quatros + numero_cincos) / 5


def main():
    
    numero_um = int(input())
    numero_dois = int(input())
    numero_tres = int(input())
    numero_quatro = int(input())
    numero_cinco = int(input())

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

