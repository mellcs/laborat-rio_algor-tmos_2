class NegativeNumberError(BaseException): 
    pass

def calculate_square_root():
    
        number = int(input("Insira um número: "))
        square_root = number ** (1/2)
        
        if number < 0: 
            raise NegativeNumberError()
        else:
            print(square_root)
    
def main():
    try:
        calculate_square_root()
        
    except NegativeNumberError:
        print("Erro! A raiz quadrada de números negativos é inválida.")
    
    except BaseException as error:
        print(f"Oorreu um erro: {error}")
    
main()
