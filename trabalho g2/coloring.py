def check_answer(word, user_attempt):

    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

    word_letters = []
    for caractere in word:
        word_letters += caractere
    
    letter1 = user_attempt[0]
    letter2 = user_attempt[1]
    letter3 = user_attempt[2]
    letter4 = user_attempt[3]
    letter5 = user_attempt[4]


    if letter1 == word[0]:
            letter1 = f'{GREEN}{user_attempt[0]}{RESET}'
    elif letter1 in word_letters:
        letter1 = f'{YELLOW}{user_attempt[0]}{RESET}'
    
    if letter2 == word[1]:
            letter2 = f'{GREEN}{user_attempt[1]}{RESET}'
    elif letter2 in word_letters:
        letter2 = f'{YELLOW}{user_attempt[1]}{RESET}'
    
    if letter3 == word[2]:
            letter3 = f'{GREEN}{user_attempt[2]}{RESET}'
    elif letter3 in word_letters:
        letter3 = f'{YELLOW}{user_attempt[2]}{RESET}'

    if letter4 == word[3]:
            letter4 = f'{GREEN}{user_attempt[3]}{RESET}'
    elif letter4 in word_letters:
        letter4 = f'{YELLOW}{user_attempt[3]}{RESET}'
    
    if letter5 == word[4]:
            letter5 = f'{GREEN}{user_attempt[4]}{RESET}'
    if letter5 in word_letters:
        letter5 = f'{YELLOW}{user_attempt[4]}{RESET}'
    
    print(f'\n| {letter1} | {letter2} | {letter3} | {letter4} | {letter5} |\n')
