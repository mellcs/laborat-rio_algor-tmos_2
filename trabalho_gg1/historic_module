def sales_report(sales_record):
    """ O registro de vendas de todos os produtos, e também registros individuais de cada produto disponível. """

    for product_name, sales in sales_record.items():
        print(f"Histórico de vendas para o produto '{product_name}':")
        for sale in sales:
            print(sale)

def alter_report(add_alter_record, value_alter_record, removal_record):
    """ A função em questão possui três opções dentro dela, que possibilitam checar as adições de produtos no estoque, atualizações de preços de produtos e exclusões de produtos. É possível fazer múltiplas checagens nessa função. """

    option = 0

    while option != 4:
        print("Históricos:")
        print("1 - Histórico de adições de produtos ao estoque.")
        print("2 - Histórico de atualizações de valores.")
        print("3 - Histórico de exclusões de produtos.")
        print("4 - Sair do menu de históricos.")

        option = int(input("Qual histórico você gostaria de acessar? "))

        if option == 1:
            for alteration in add_alter_record:
                print(alteration)

        elif option == 2:
            for alteration in value_alter_record:
                print(alteration)

        elif option == 3:
            for alteration in removal_record:
                print(alteration)

        elif option == 4:
            break
        
        else:
            print("Insira uma opção válida.")

