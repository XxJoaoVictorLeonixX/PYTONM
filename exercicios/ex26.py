sal = float(input('Informe o seu salario:'))
if sal > 1250:
    aumento = sal*0.10
    novo = aumento + sal
    print('O seu aumento 10% {}, seu novo salario R${}'.format(aumento,novo))
else:
    aumento = sal*0.15
    novo = aumento + sal
    print('Aumento do salario com 15% R${}, seu novo salario R${} '.format(aumento,novo))