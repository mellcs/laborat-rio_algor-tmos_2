class InvalidOption(BaseException):
   """Exception created to prevent the user from choosing an option that doesn't exist."""
   pass 

def Menu():
    """Regular menu, with three exceptions to prevent errors."""
    print("MENU")
    print("1 - Depositar dinheiro.")
    print("2 - Sacar dinheiro.")
    print("3 - Verificar saldo bancário.")
    print("4 - Histórico de movimentações.")
    print("5 - Sair.")
    
    try:
        option = int(input("O que você gostaria de fazer?"))
        
        if option <1 or option >5:
            raise InvalidOption
        
        return option
        
    except ValueError:
        print("Insira um número inteiro disponível no menu.")
    except InvalidOption:
        print("Insira uma opção disponível no menu.")
    except BaseException as error:
        print(f"Erro! {error}.")
  
def Deposit_Money():
    """Function created to deposit money on the bank"""

def main():
    """Main that calls the other funtions and treats a few errors"""
    while True:
        menu()
        
        if option == 1:
            
    
    
    
main()
