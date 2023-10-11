def division():
    while True:
        try:
            number1 = int(input("Insira o primeiro número:"))
            number2 = int(input("Insira o segundo número:"))
            
            divisao = number1 / number2
            
            print(divisao)
        except ZeroDivisionError:
            print("Erro! Não é possível dividir por 0.")
        except ValueError:
            print("Erro! É possível que você tenha tentado inserir uma letra ao invés de um número, ou um número decimal. É necessário inserir um número inteiro.")
        except BaseException as error:
            print(f"Erro! {error}")
        finally: 
            print("Aguarde um instante!")

division()
