hora = int(input("Digite quantos horas são: "))
minuto = int(input("Digite quantos minutos são: "))
segundo = int(input("Digite quantos segundos são: "))

hora_minuto = hora * 60
minuto_segundo = (hora_minuto + minuto) * 60
segundo_totais = minuto_segundo + segundo

print(f"Desde a última noite, passaram {segundo_totais:.2f} segundos")
