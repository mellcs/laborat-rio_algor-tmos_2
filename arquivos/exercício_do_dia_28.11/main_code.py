def funcao_top(names_file, grades_file):
    students_names = names_file.readlines()
    students_grades = grades_file.readlines()

    for i in range(len(students_names)):
        current_grades = students_grades[i].split()
        sum = 0 

        for e in range(len(current_grades)):
            sum = sum + int(current_grades[e])
        
        print(students_names[i], sum, current_grades, sum/len(current_grades))


def main():
    names_file = open("students_names.txt")
    grades_file = open("students_grades.txt")

    funcao_top(names_file, grades_file)


main()
