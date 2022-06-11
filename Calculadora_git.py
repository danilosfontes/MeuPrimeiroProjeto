x = 0

while x == 0:
    num1 = int(input('Insira um número:\n'))
    num2 = int(input('Insira outro número\n'))
    operador = input('Digite o operador desejado: (+-*/)')
    if operador == '+':
        print('{:.2f}'.format(num1 + num2))
    elif operador == '-':
        print('{:.2f}'.format(num1 - num2))
    elif operador == '*':
        print('{:.2f}'.format(num1 * num2))
    elif operador == '/':
        print('{:.2f}'.format(num1 / num2))
    else:
        print('Operador inválido, por favor digite um operador válido(+,-,*,/) Obrigado')
    reset = input('Deseja realizar outra operação? (s/n)')
    reset = reset.lower()
    if reset == 'n':
        x = 1
        print('Obrigado, Volte Sempre')
