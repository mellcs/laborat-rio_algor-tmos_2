def get_month_name(month):
    try:
        months = (
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        )
        
        return months[month - 1]
    except IndexError:
        print("Erro! Insira um mês existente!")
    
        
    except BaseException as error:
        print(f"Erro! {error}")
    
    
class InvalidMonthException(BaseException):
    pass
    
def main():
    try:
        month = int(input("Insira o mês:"))
        
        if month >12 or month < 1:
            raise InvalidMonthException()
        
        month_name = get_month_name(month)
        
        print(f"Nome do mês: {month_name})
    
    except ValueError:
        print("Erro! Digite apenas números inteiros!")
    except InvalidMonthException:
        print("O mês informado não existe.")
    except BaseException as error:
        print(f"Erro! {error}")
    
main()
