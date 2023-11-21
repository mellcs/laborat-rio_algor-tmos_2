def menu(message):

    try:

        print(message)
        print('>>> MENU DO JOGO TERMO <<<')
        print('1 - Jogar')
        print('2 - Resetar palavras já utilizadas')
        print('3 - Sair')
        print()

        option = int(input("Selecione uma opção: "))

        assert option == 1 or option == 2 or option == 3, 'Você deve selecionar uma opção válida!'

        return option
    
    except AssertionError:
        option = menu('Erro! Você deve selecionar uma opção válida!')
        return option
    
    except TypeError:
        option = menu('Erro! Você deve selecionar uma opção válida!')
        return option
    
    except ValueError:
        option = menu('Erro! Você deve selecionar uma opção válida!')
        return option
    
    except BaseException as error:
        option = menu(f'Erro! {error}')
        return option
