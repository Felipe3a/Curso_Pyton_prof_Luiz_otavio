hora  = input('Por favor, digite a hora atual (0-23): ')

hora_float = float(hora)

if hora_float >= 0 and hora_float <= 11.59:
    print('Bom dia!')
elif hora_float >= 12 and hora_float <= 17.59:
    print('Boa tarde!')
elif hora_float >= 18 and hora_float <= 23.59:
    print('Boa noite!')     