import random
import menu

def get_secret_word():
    with open("word_list.txt", "r") as file:
        word_list = file.readlines()
        variable = random.choice(word_list).strip()
        variable = variable.lower()
        return variable

def load_used_words():
    try:
        with open("guessed_words.txt", "r") as file:
            used_words = [line.strip() for line in file.readlines()]
        return used_words
    except FileNotFoundError:
        return []

def save_used_words(guess_lower):
    with open("guessed_words.txt", "a") as file:
        file.write(guess_lower + '\n')

def start(secret_word, guess_counter):
    print("Bem-vindo ao jogo Termo!")
    print("Tente adivinhar a palavra secreta de 5 letras")

    secret_word_lower = secret_word.lower()
    used_words = []

    while guess_counter > 0:
        guess = input("Faça seu palpite: ")

        if len(guess) != 5:
            print("Insira uma palavra de 5 letras, sem números, acentos ou espaços.")
            continue

        guess_lower = guess.lower()
        result = []

        if guess_lower in used_words:
            print("Você já tentou essa palavra. Tente outra.")
            continue

        used_words.append(guess_lower)

        for i in range(len(guess_lower)):
            if guess_lower[i] == secret_word_lower[i]:
                result.append('\033[92m' + guess_lower[i] + '\033[0m')
                used_words.append(guess_lower[i])
            else:
                result.append(guess_lower[i])

        for j in range(len(guess_lower)):
            if guess_lower[j] in secret_word_lower and guess_lower[j] not in used_words:
                result[j] = '\033[93m' + guess_lower[j] + '\033[0m'
                used_words.append(guess_lower[j])

        for x in range(len(guess_lower)):
            if guess_lower[x] not in secret_word_lower or (
                    guess_lower[x] in secret_word_lower and guess_lower[x] not in used_words):
                result[x] = '\033[97m' + guess_lower[x] + '\033[0m'

        print(f"{result[0]}|{result[1]}|{result[2]}|{result[3]}|{result[4]}")

        if result == [f"\033[92m{c}\033[0m" if c in secret_word_lower else c for c in guess_lower]:
            print("Parabéns! Você acertou a palavra secreta.")
            save_used_words(secret_word_lower)
            main()
            return True

        guess_counter -= 1
        print(f"Tentativas restantes: {guess_counter}")

    print(f"Fim do jogo! A palavra secreta era: {secret_word}")
    save_used_words(guess_lower)
    main()
    return False

def main():
    menu.menus()

    guess_counter = 5
    secret_word = get_secret_word()
    while guess_counter > 0:
        if start(secret_word, guess_counter):
            break  # Sai do loop principal se o jogador acertar a palavra
        guess_counter -= 1
    

main()
