def exibir_menu():
    """Exibe o menu de opções da calculadora."""
    print("\n****** Menu Calculadora ******")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def obter_numero(mensagem):
    """Pede um número ao usuário e garante que seja válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Insira apenas números válidos.")

def calcular(opcao, num1, num2):
    """Realiza a operação matemática baseada na escolha do usuário(usando dicionário)."""
    operacoes = {
        '1': ("Soma", num1 + num2),
        '2': ("Subtração", num1 - num2),
        '3': ("Multiplicação", num1 * num2),
        '4': ("Divisão", "Erro: Divisão por zero!" if num2 == 0 else num1 / num2)
    }
    nome, resultado = operacoes.get(opcao, ("Opção inválida!", None))
    print(f"Resultado da {nome}: {resultado}")

def main():
    """Executa a calculadora com interação contínua até que o usuário escolha sair."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma operação: ")

        if opcao == '5':
            print(" Obrigada por utilizar a calculadora!")
            break
        
        if opcao in ['1', '2', '3', '4']:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            calcular(opcao, num1, num2)
        else:
            print(" Opção inválida! Tente novamente.")

        if input("\nDeseja realizar outra operação? (s para sim / n para não): ").lower() != "s":
            print(" Obrigada por utilizar a calculadora!")
            break

# Execução da calculadora
if __name__ == "__main__":
    main()
