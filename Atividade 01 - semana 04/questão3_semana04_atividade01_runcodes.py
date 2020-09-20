def maior(numero_ums, numero_doiss, numero_tress, numero_quatros, numero_cincos):
    if numero_ums > numero_doiss and numero_ums > numero_tress and numero_ums > numero_quatros and numero_ums > numero_cincos:
        return numero_ums
    if numero_doiss > numero_ums and numero_doiss > numero_tress and numero_doiss > numero_quatros and numero_doiss > numero_cincos:
        return numero_doiss
    if numero_tress > numero_ums and numero_tress > numero_doiss and numero_tress > numero_quatros and numero_tress > numero_cincos:
        return numero_tress
    if numero_quatros > numero_ums and numero_quatros > numero_doiss and numero_quatros > numero_tress and numero_quatros > numero_cincos:
        return numero_quatros
    if numero_cincos > numero_ums and numero_cincos > numero_doiss and numero_cincos > numero_tress and numero_cincos > numero_quatros:
        return numero_cincos
    else:
        return 'Erro'

def menor(numero_ums, numero_doiss, numero_tress, numero_quatros, numero_cincos):
    if numero_ums < numero_doiss and numero_ums < numero_tress and numero_ums < numero_quatros and numero_ums < numero_cincos:
        return numero_ums
    if numero_doiss < numero_ums and numero_doiss < numero_tress and numero_doiss < numero_quatros and numero_doiss < numero_cincos:
        return numero_doiss
    if numero_tress < numero_ums and numero_tress < numero_doiss and numero_tress < numero_quatros and numero_tress < numero_cincos:
        return numero_tress
    if numero_quatros < numero_ums and numero_quatros < numero_doiss and numero_quatros < numero_tress and numero_quatros < numero_cincos:
        return numero_quatros
    if numero_cincos < numero_ums and numero_cincos < numero_doiss and numero_cincos < numero_tress and numero_cincos < numero_quatros:
        return numero_cincos
    else:
        return 'Erro'
def main():
    numero_um = int(input())
    numero_dois = int(input())
    numero_tres = int(input())
    numero_quatro = int(input())
    numero_cinco = int(input())

    maior_numero = maior(numero_um, numero_dois, numero_tres, numero_quatro, numero_cinco)
    menor_numero = menor(numero_um, numero_dois, numero_tres, numero_quatro, numero_cinco)

    print(f'{maior_numero}')
    print(f'{menor_numero}')

if __name__ == '__main__':
        main()
