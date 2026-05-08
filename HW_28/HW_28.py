'''Анализ курсов студентов
Реализовать программу, которая должна:
Прочитать файл student_courses.json, содержащий:
имя,
дату рождения (birth_date) в формате дд.мм.гггг,
дату поступления (enrollment_date) в том же формате,
список курсов.
Вычислить:
Общее количество студентов.
Средний возраст на момент поступления.
Сохранить отчёт в JSON-файл student_courses_report.json.'''

import json
from datetime import datetime

with open("HW\HW_28\student_courses.json", "r", encoding="utf-8") as file:
    students = json.load(file)
    
total_students = len(students)
total_age = 0

for student in students:
    birth_date = datetime.strptime(student["birth_date"], "%d.%m.%Y")
    enrollment_date = datetime.strptime(student["enrollment_date"], "%d.%m.%Y")
    
    age = enrollment_date.year - birth_date.year
    
    if (enrollment_date.month, enrollment_date.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    total_age += age
    
avg_age = total_age / total_students
avg_age = round(avg_age, 1)

report = {
    "total_students": total_students,
    "average_enrollment_age": avg_age
}

with open("HW\HW_28\student_courses_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=4)