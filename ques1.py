# Given the names and grades for each student in a class of  students
# , store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

students_grade = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students_grade.append([name,score])
        
sorted_scores = sorted(list(set([x[1] for x in students_grade])))
second_lowest_score = sorted_scores[1]

low_final_list = []
for student in students_grade:
    if second_lowest_score == student[1]:
        low_final_list.append(student[0])
            
for student in sorted(low_final_list):
    print(student)

