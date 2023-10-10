def division(val1, val2):
    
    try:
        return val1/val2
    except ZeroDivisionError:
        print('[Erro] Você não pode dividir um número por zero!')
        raise 
    except BaseException as error:
        print(f'[Erro] Ocorreu um erro: {error}')
        

def input_int(message, canBeZero):
    while True:
        try:
            value = int(input(message))
            
            if not canBeZero and value == 0:
                raise ValueError()
            
            
            return value
        except ValueError:
            print("Ocorreu um erro.")
        except BaseException as error:
            print(f"Oorreu um erro: {error}")
        finally:
            print("Pressione qualquer letra para continuar")
            os.system("cls")
            print("finally hehe")
       
    
    
def main():
    
    try:    
        number_one = input_int("Digite o primerio valor")
        number_two = input_int("Digite o segundo valor", canBeZero=False)
        
        #if number_two = 0:
            #raise ValueError
    
        result = division(number_one,number_two)
        
        print(f'Resultado: {result}')
    
    except ValueError:
        print("Número informado inválido.")
    except BaseException as error:
        print(f"Ocorreu um erro: {error}")
    else:
        print("dyva!!!")
        
main()
