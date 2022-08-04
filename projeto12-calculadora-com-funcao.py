'''Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação
e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

Passos:
    escrever função matemática com condicionais de operação
    solicitar ao usuário os dados
    apresentar o resultado'''


# Função
def operacao(t1, t2, op):
    if (op == 1):
        return (t1 + t2)
    elif (op == 2):
        return (t1 - t2)
    elif (op == 3):
        return (t1 * t2)
    elif (op == 4):
        return (t1 / t2)
    else:
        return (0)


# Programa
t1 = int(input("Informe o primeiro valor: "))
t2 = int(input("Informe o segundo valor: "))
op = int(input('Informe a operação: \n[1-Soma]\n[2-Subtração]\n[3-Multiplicação]\n[4-Divisão] '))
print(f'Resultado: {operacao(t1, t2, op)}')
