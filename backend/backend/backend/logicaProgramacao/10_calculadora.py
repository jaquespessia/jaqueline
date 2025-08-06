num1 = int (input("digite um numero:"))
num2 = int (input("digite outro numero:"))

operacao = input("escolha uma operacao (+,-,*,/):")
match operacao :
    case "+":
        soma = num1 + num2
        print("o resultado é", soma)

    case "-":
        subtracao = num1 - num2
        print("o resultado é", subtracao)

    case "*":
        multiplicacao = num1 * num2
        print("o resultado é", multiplicacao)

    case "/":
        divisao = num1 / num2
        print("o resultado é", divisao)
