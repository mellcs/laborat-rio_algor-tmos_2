def verify_troco(saque):
    contador100 = 0
    contador50 = 0
    contador20 = 0
    contador10 = 0
    while saque >= 100:
        contador100 += 1
        saque -= 100
    while saque >= 50:
        contador50 += 1
        saque -= 50
    while saque >= 20:
        contador20 += 1
        saque -= 20
    while saque >= 10:
        contador10 += 1
        saque -= 10
    return contador100, contador50, contador20, contador10

def main():
    saque = float(input("Digite o valor do saque: "))
    if saque % 10 != 0:
        while saque % 10 != 0:
            saque = float(input("Digite o valor do saque: " ))
    print("teste")
    contador100 = 0
    contador50 = 0
    contador20 = 0
    contador10 = 0
    contador100, contador50, contador20, contador10 = verify_troco(saque)
    print(f"Valor do saque: R$ {saque}, - Resultado esperado: Entregar {contador100} notas de R$100,00. {contador50} notas de R$50,00. {contador20} notas de R$20,00. {contador10} notas de R$10,00" ) 



main()
