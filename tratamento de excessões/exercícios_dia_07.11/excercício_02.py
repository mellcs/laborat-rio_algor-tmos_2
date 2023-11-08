def rating():
    try:
        rate = int(input("Avalie o produto: "))
        
        assert rate >= 0 and rate <= 10
        print("Obrigada pela avaliação!")
        
    except AssertionError:
        print("O número está acima do permitido!")
        

def main():
    rating()
    
main()
