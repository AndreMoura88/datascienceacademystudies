# Calculadora em Python
print('*' * 10, 'Python Calculator', '*' * 10)

print("Selecione o número da operação desejada:")
print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
operador = 'Operação inválida'
c = 0
x = int(input(("Digite sua opção (1/2/3/4):")))
if 1 <= x <= 4:
    a = float(input(("Digite o primeiro número:")))
    b = float(input(('Digite o segundo número:')))
    if x == 1:
        c = a + b
        operador = '+'
    elif x == 2:
        c = a - b
        operador = '-'
    elif x == 3:
        c = a * b
        operador = '*'
    elif x == 4:
        c = a / b
        operador = '/'
    print("A sua operação é:")
    print(f"{a} {operador} {b} = {round(c, 2)}")
else:
    print('Opção inválida')