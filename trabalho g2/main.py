import menu
import gameplay

def main():

    while True:

        for _ in range(1):
            opc = menu.menu('')

            if opc == 1:
                gameplay.play()

            elif opc == 2:
                file = open('used_words.txt', 'w')
                file.close()

            elif opc == 3:
                break

main()
