#for, [],.upper,.sort, while

def hamsters():
    ask = int(input("Which hamster would you like to know?"))
    if ask == 1:
        print("Hamster number one is named Lini!")
    elif ask == 2:
        print("Hamster number two is named Rita!")
    elif ask == 3:
        print("Hamster number three is named Lia!")
    elif ask == 4:
        print("Hamster number four is named Mork!")
    elif ask ==5:
        print("Hamster five is named Chilton!")
    else:
        print("There are only five hamsters.")
    return ask
    
def respect_ask():
    print("These are the offerings:")
    print("1- Giving seeds.")
    print("2- Giving sand.")
    print("3- Giving lettuce.")
    opt_respect = int(input("How would you like to pay respects?"))
    if opt_respect == 1:
        print("The hamsters bless you with full cheeks.")
    elif opt_respect == 2:
        print("The hamsters bless you with clean skin.")
    elif opt_respect == 3:
        print("The hamsters bless you with a full belly.")
    else:
        print("These are the only available ones, sorry.")
    return opt_respect
    
def menu():
    print("1- Choose a hamster?")
    print("2- Pay respect to hamster?")
    print("3- Leave?")

def main ():
    menu()
    opt = int(input("What would you like to do?"))
    if opt == 1:
        hamsters()
    elif opt == 2:
        respect_ask()
    elif opt == 3:
        print("Have a blessed life, hooman!")
    else:
        print("Choose a valid option.")
        
        
main()