velo = float(input('Informe a velocidade do carro:'))
if velo > 80:
    print('Você foi multado:')
    multa = (velo-80)*7
    print('A sua multa é de R${.:2f}:'.format(multa))
else:
    print('Você esta dentro do limite permitido de velocidade mantenha assim!')
