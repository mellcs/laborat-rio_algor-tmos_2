def show_menu():
  """ Mostra todas as funcionalidades do programa e permite o acesso aos módulos e funções. """
  print("\t Menu Principal") 
  print("1 - Adicionar um produto.")
  print("2 - Alterar o valor de um produto.")
  print("3 - Excluir um produto.")
  print("4 - Histórico de alterações.")
  print("5 - Buscar um produto.")
  print("6 - Buscar produto por categoria.")
  print("7 - Visualizar todos os produtos.")
  print("8 - Vender um produto.")
  print("9 - Relatório de vendas.")
  print("10 - Sair.")

  option = int(input("\n Digite a opção que deseja executar: "))

  return option
