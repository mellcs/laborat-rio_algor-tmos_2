class ContaBancaria:
    def depositar(conta, valor):
        try:
            valor = float(valor)
            if valor > 0:
                conta['saldo'] += valor
                conta['movimentacoes'].append(f'Depósito: +{valor}')
                print(f'Depósito de {valor} realizado com sucesso.')
            else:
                raise ValueError('Valor do depósito deve ser positivo.')
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira um valor numérico válido.")

    def sacar(conta, valor):
        try:
            valor = float(valor)  
            if valor > 0 and valor <= conta['transaction_limit'] and valor <= conta['saldo']:
                conta['saldo'] -= valor
                conta['movimentacoes'].append(f'Saque: -{valor}')
                print(f'Saque de {valor} realizado com sucesso.')
            else:
                raise ValueError('Saque inválido. Verifique o valor ou seu limite.')
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira um valor numérico válido.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero.")
        except IndexError:
            print("Erro: Índice inválido.")
        except KeyError:
            print("Erro: Chave inexistente no dicionário.")

    def verificar_saldo(conta):
        print(f'Saldo atual: {conta["saldo"]}')

    def historico_movimentacoes(conta):
        print('Histórico de movimentações:')
        for movimentacao in conta['movimentacoes']:
            print(movimentacao)

def main():
    conta = {'saldo': 0, 'movimentacoes': [], 'transaction_limit': 10000}
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar dinheiro")
        print("2 - Sacar dinheiro")
        print("3 - Verificar saldo bancário")
        print("4 - Histórico de movimentações")
        print("5 - Sair")
    
        try:
            opcao = int(input("Digite o número da opção desejada: "))
    
            if opcao == 1:
                valor = input("Digite o valor a ser depositado: ")
                ContaBancaria.depositar(conta, valor)
            elif opcao == 2:
                valor = input("Digite o valor a ser sacado: ")
                ContaBancaria.sacar(conta, valor)
            elif opcao == 3:
                ContaBancaria.verificar_saldo(conta)
            elif opcao == 4:
                ContaBancaria.historico_movimentacoes(conta)
            elif opcao == 5:
                print("Saindo do sistema. Até logo!")
                break
            else:
                raise ValueError("Opção inválida. Tente novamente.")
        except ValueError as e:
            print(e)
        except BaseError as error:
            print("Erro!")

main()


            
    
    
    
main()
