def triangles(triangle_side_1, triangle_side_2, triangle_side_3):
    if triangle_side_1 == triangle_side_2 and triangle_side_1 == triangle_side_3 and triangle_side_2 == triangle_side_3:
        print("É um triângulo equilátero.")
    
    elif triangle_side_1 == triangle_side_2 or triangle_side_1 == triangle_side_3 or triangle_side_2 == triangle_side_3:
        print("É um triângulo isósceles.")
    
    elif triangle_side_1 != triangle_side_2 and triangle_side_1 != triangle_side_3 and triangle_side_2 != triangle_side_3:
        print("É um triângulo escaleno.")
    
    else:
        print("hehe")

def additions(triangle_side_1, triangle_side_2, triangle_side_3):
    biggest = 0
    middle = 0
    smallest = 0
    
    if triangle_side_1 > triangle_side_2 and triangle_side_1 > triangle_side_3:
        biggest = triangle_side_1
        if triangle_side_2 > triangle_side_3:
            middle = triangle_side_2
            smallest = triangle_side_3
        else:
            middle = triangle_side_3
            smallest = triangle_side_2
    if triangle_side_2 > triangle_side_1 and triangle_side_2 > triangle_side_3:
        biggest = triangle_side_2
        if triangle_side_1 > triangle_side_3:
            middle = triangle_side_1
            smallest = triangle_side_3
        else:
            middle = triangle_side_3
            smallest = triangle_side_1
    if triangle_side_3 > triangle_side_2 and triangle_side_3 > triangle_side_1:
        biggest = triangle_side_3
        if triangle_side_2 > triangle_side_1:
            middle = triangle_side_2
            smallest = triangle_side_1
        else:
            middle = triangle_side_1
            smallest = triangle_side_2
    
    sum_sides = middle + smallest
    if sum_sides < biggest:
        raise ValueError()


def main():
    try:
        triangle_side_1 = float(input("Insira o tamanho do primeiro lado do triângulo: "))
        triangle_side_2 = float(input("Insira o tamanho do segundo lado do triângulo: "))
        triangle_side_3 = float(input("Insira o tamanho do terceiro lado do triângulo: "))
        additions(triangle_side_1, triangle_side_2, triangle_side_3)
        triangles(triangle_side_1, triangle_side_2, triangle_side_3)

    except ValueError:
        print("O triângulo informado é inválido!")

    except BaseException as error:
            print(f"Oorreu um erro: {error}")
    
main()  
