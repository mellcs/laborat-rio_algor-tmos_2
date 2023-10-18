def is_leap_year(year):
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        return True

        return False

def main():
    try:
        year = int(input("Digite um ano:"))
        
        result = is_leap_year(year)
        
        print("É bissexto?", result)
        
    except ValueError:
        print("Erro! Valor digitado inválido!")
    except BaseException as error:
        print("Erro! Ocorreu um erro.", error)

main()
