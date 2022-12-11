casa = float(input('Informe o valor da casa R$:'))
salario = float(input('Informe o seu salario R$:'))
anos = int(input('Informe anos de financiamento:'))
presta = casa / (anos * 12)
min = salario * 30 /100
print('Para pagar uma casa  de R${:.2f} em {} anos'.format(casa,anos))
print('A prestação  sera  de R${:.2f}'.format(presta))

if presta <= min:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo negado!')
