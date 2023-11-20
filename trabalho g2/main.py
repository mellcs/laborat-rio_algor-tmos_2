from menu import menus
import working_code

def main():
    
    while True:
        option = menus()
        
        if option == 1:
            secret_word = working_code.get_secret_word()
            guess_counter = 5
            working_code.start(secret_word, guess_counter)

        elif option == 2:
            print("indos")

        elif option == 3:
            print("hoho")
        
        elif option == 4:
            print("hoo")
        
        elif option == 5:
            working_code.register_guessed_words()
    
main()
