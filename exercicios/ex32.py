n1 = float(input('Informe a primeira nota:'))
n2 = float(input('Informe a segunda nota:'))
media = (n1 + n2) / 2

if media < 5:
    print('Você esta reprovado!')
elif media >= 5 and media < 6.9:
    print('Você esta de recuperação!')
elif media >=7:
    print('APROVADO!')