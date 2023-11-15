def calculate_avg():
    my_file = open("exercícios/numbers.txt", "r")
    file_content = my_file.read()
    numbers_list = file_content.split(",")

    sum_of_numbers = 0

    for number in numbers_list:
        sum_of_numbers += int(number)

    
    print(sum_of_numbers / len(numbers_list))
    #print(file_content, numbers_list, sum_of_numbers)

def main():
    result = calculate_avg()
    print("Média:", result)
main()
