import random

def verify_word(word):
    
    used_words_file = open('used_words.txt', 'r')
    if word in used_words_file:
        word = sort_word()
        used_words_file.close()
        return True
    used_words_file.close()

def sort_word():

    words_file = open('words.txt', 'r')
    number = random.randint(0, 100)
    for _ in range(number):
        word = words_file.readline().rstrip('\n')
    words_file.close()

    if verify_word(word):
        word = sort_word()

    return word.upper()

def user_input(used_words):

    try:
        input_word = str(input("Digite uma palavra: ")).upper()

        assert len(input_word) == 5, 'A palavra digitada deve ter 5 letras! '
        assert verify_digits(input_word) == False, 'Você não pode digitar números!'
        assert verify_space(input_word) == False, 'Você não pode deixar espaços em branco!'
        assert input_word not in used_words, 'Você não pode usar a mesma palavra mais de uma vez em um jogo!'

        return input_word.upper()
    
    except AssertionError as error:
        print(f'[ERRO] {error}')
        input_word = user_input(used_words)
        return input_word
    
    except BaseException as error:
        print(f'[ERRO] Um erro ocorreu: {error}')
        input_word = user_input(used_words)
        return input_word

def verify_digits(word):

    for caractere in word:
        if caractere.isdigit():
            return True
        
    return False

def verify_space(word):

    for caractere in word:
        if caractere.isspace():
            return True
        
    return False
