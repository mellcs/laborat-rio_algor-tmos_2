import verification_and_input
import coloring

def play():

    attempt_counter = 4
    current_attemps = 0

    used_words = []
    secret_word = verification_and_input.sort_word()
    user_attempt = ''

    while secret_word != user_attempt:
        if current_attemps <= attempt_counter:
            while current_attemps <= attempt_counter:

                user_attempt = verification_and_input.user_input()

                used_words += [user_attempt]
                current_attemps += 1

                coloring.check_answer(secret_word, user_attempt)

                if user_attempt == secret_word:

                    print('Parabéns! Você ganhou!')
                    file = open('used_words.txt', 'a')
                    file.write(str(f'{secret_word}\n'))
                    file.close()
                    break

        else:

            print('Que pena, você perdeu!')
            print(f'A palavra correta era: {secret_word}')
            break
