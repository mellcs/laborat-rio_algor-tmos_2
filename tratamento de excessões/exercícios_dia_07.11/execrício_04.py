def find_element(my_list, index):
    try:
        result = my_list[index]
        print(result)
    except IndexError:
        print("Erro! O índice informado é inválido.")
    
def main():
    try:
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        index = int(input("Insira o índice desejado: "))
        find_element(my_list, index)
    except IndexError as error:
        print(error)
    

main()
