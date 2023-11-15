def check_text(word):
    my_file = open("exercícios/bees text.txt", "r")
    lines_list = my_file.readlines()

    for line in lines_list:
        if word in line:
            print(line)
    

def main():
    word = input("Insira uma palavra para verificar se está presente no texto: ")
    check_text(word)


main()
