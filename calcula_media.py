def calculadora():
    while True:
        try:
            expressao = input("Digite a operação matemática (ou 'sair' para encerrar): ")
            if expressao.lower() == 'sair':
                print("Encerrando a calculadora...")
                break
            resultado = eval(expressao)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")

if __name__ == "__main__":
    calculadora()
