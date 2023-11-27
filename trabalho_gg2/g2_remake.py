import random

def colorinho(secret_word, user_attempt):
    WHITE = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

    word_letters = []

    for letter in secret_word:
        word_letters += letter
    
    letter1 = user_attempt[0]
    letter2 = user_attempt[1]
    letter3 = user_attempt[2]
    letter4 = user_attempt[3]
    letter5 = user_attempt[4]


    if letter1 == secret_word[0]:
            letter1 = f'{GREEN}{user_attempt[0]}{WHITE}'
    elif letter1 in word_letters:
        letter1 = f'{YELLOW}{user_attempt[0]}{WHITE}'
    
    if letter2 == secret_word[1]:
            letter2 = f'{GREEN}{user_attempt[1]}{WHITE}'
    elif letter2 in word_letters:
        letter2 = f'{YELLOW}{user_attempt[1]}{WHITE}'
    
    if letter3 == secret_word[2]:
            letter3 = f'{GREEN}{user_attempt[2]}{WHITE}'
    elif letter3 in word_letters:
        letter3 = f'{YELLOW}{user_attempt[2]}{WHITE}'

    if letter4 == secret_word[3]:
            letter4 = f'{GREEN}{user_attempt[3]}{WHITE}'
    elif letter4 in word_letters:
        letter4 = f'{YELLOW}{user_attempt[3]}{WHITE}'
    
    if letter5 == secret_word[4]:
            letter5 = f'{GREEN}{user_attempt[4]}{WHITE}'
    if letter5 in word_letters:
        letter5 = f'{YELLOW}{user_attempt[4]}{WHITE}'
    
    print(f'\n| {letter1} | {letter2} | {letter3} | {letter4} | {letter5} |\n')

def draw_word():
    my_file = open("words.txt", "r")

    lines = my_file.read()
    list_words = lines.split('\n')
    secret_word = random.choice(list_words)

    # for i in range(number):
    #     secret_word = my_file.readline().rstrip('\n') 
    if check_word(secret_word):
        secret_word = draw_word()
    my_file.close()
    return secret_word.lower()

def check_word(secret_word):
    used_words_file = open("used_words.txt", "r")
    if secret_word in used_words_file:
        secret_word = draw_word()
        used_words_file.close()
        return True
    used_words_file.close()

def check_for_numbers(user_attempt):
    for letter in user_attempt:
        if letter.isdigit():
            return True 
    return False 

def check_for_space(user_attempt):
    for letter in user_attempt:
        if letter.isspace():
            return True 
    return False 

def add_word(word):
    file = open('used_words.txt', 'a')
    
    file.write(str(f'{word}\n'))

    file.close()

    return True

def check_user_attempt(user_attempt, used_words):

    if len(user_attempt) != 5:
        print('A palavra digitada deve ter 5 letras! ')
        return False

    elif check_for_numbers(user_attempt):
        print("Apenas letras sem número são permitidas.")
        return False

    elif check_for_space(user_attempt):
        print('Apenas letras sem espaços são permitidas.')
        return False

    elif user_attempt in used_words: 
        print('Você só pode usar uma palavra uma vez por jogo.')
        return False
    
    return True


def start_the_game(user_attempt):
    attempt_counter = 5
    used_words = []
    secret_word = draw_word()

    while True:
        user_attempt = input("Insira a tentativa: ").lower()

        if check_user_attempt(user_attempt, used_words):
            used_words.append(user_attempt)
            attempt_counter -= 1
            colorinho(secret_word, user_attempt)

            if user_attempt == secret_word:
                print("Parabéns! Você ganhou o jogo!")
                add_word(secret_word)
                return  
        else: 
            continue

        if attempt_counter == 0:
             break
        
    print("Você perdeu!") 
    print(f"A palavra secreta era: {secret_word}")


def main(): 
    secret_word = draw_word()

    while True:
        print("~ MENU ~")
        print("1 - Jogar Termo.")
        print("2 - Resetar palavras.")
        print("3 - Sair.\n")
        
        try:
            option = int(input("O que você gostaria de fazer? "))
            
        except ValueError:
             print("Responda apenas com números.")
             continue

        if option == 1:
            secret_word = draw_word()
            used_words = []
            start_the_game(user_attempt="")

        elif option == 2:
            my_file = open('used_words.txt', 'w')
            my_file.close()

        elif option == 3:
            print("Obrigada por jogar!")
            break
        else:
            print("Resposta inválida, insira uma opção disponível.")

main()
