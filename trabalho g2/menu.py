def menus():
    while True:
        print(">>>>MENU<<<<")
        print("1 - Jogar.")
        print("2 - Redefinir palavras.")
        print("3 - Resetar o jogo.")
        print("4 - Sair.")
        print("5 - Ver palavras adivinhadas.")

        try:
            option = int(input("O que você gostaria de fazer? "))
        except ValueError:
            print("Erro! Insira um número.")
            continue

        if option == 1:
            return option
        
        elif option == 2:
            print("hehe")

        elif option == 3:
            print("jamais")

        elif option == 4:
            print("Obrigada por jogar!")
            exit()

        elif option == 5:
            return option
        
        else:
            print("Opção inválida. Escolha novamente.")
