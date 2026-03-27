## Student Grade Calculator

student_grades = {}

def gradeCalculator():

    student_id = len(student_grades) + 1

    student_grade = {}

    name = input("Input your name: ")
    print("Please input 3 assignment scores 0-100.")
    assign_score_1 = input("Assignment score 1: ")
    assign_score_2 = input("Assignment score 2: ")
    assign_score_3 = input("Assignment score 3: ")

    try:
        s1 = int(assign_score_1)
        s2 = int(assign_score_2)
        s3 = int(assign_score_3)
    except ValueError:
        print("Invalid score. Please use whole numbers!")
        return
    else:
        if not (0 <= s1 <= 100 and 0 <= s2 <= 100 and 0 <= s3 <= 100):
            print("Invalid score. Scores must be between 0 and 100!")
            return
        
        avg_score = (s1 + s2 + s3)/3

        student_grade["Name"] = name
        student_grade["Score 1"] = s1
        student_grade["Score 2"] = s2
        student_grade["Score 3"] = s3
        student_grade["Average Score"] = round(avg_score, 2)

        student_grades[f"Student {student_id}"] = student_grade

        print(
        "---Summary of details---\n" 
        f"Name: {name}\n" 
        "---Scores---\n"
        f"Score 1: {s1}\n"
        f"Score 2: {s2}\n"
        f"Score 3: {s3}\n" 
        f"Average Score: {round(avg_score, 2)}"
        )

gradeCalculator()