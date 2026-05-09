import csv
import statistics

BASE_PATH = "HW/HW_29"

with open(f"{BASE_PATH}/grades.csv", "r", encoding="utf-8-sig", newline="") as file_f1:
    reader_f1 = csv.DictReader(file_f1)
    rows_f1 = list(reader_f1)
    
subjects = []

for row_f1 in rows_f1:
    subject_f1 = row_f1["subject"]    
    if subject_f1 not in subjects:
        subjects.append(subject_f1)
        
for subject in subjects:
    filename_f2 = f"grades-{subject}.csv"
    
    with open(f"{BASE_PATH}/{filename_f2}", "w", newline="") as file_f2:
        writer_f2 = csv.writer(file_f2)
        
        writer_f2.writerow(["name", "grade"])
        
        for row_f1 in rows_f1:
            if row_f1["subject"] == subject:
                name_f1 = row_f1["name"]
                grade_f1 = row_f1["grade"]
                
                writer_f2.writerow([name_f1, grade_f1])
                
                
with open(f"{BASE_PATH}/grades-info.csv", "w", newline="") as file_info:
    writer_info = csv.writer(file_info)
    writer_info.writerow([
        "Subject",
        "Mean",
        "Min",
        "Max",
        "Median",
        "Stdev"
    ])
    
    for subject in subjects:
        grades_list = []
        for row_f1 in rows_f1:
            if row_f1["subject"] == subject:
                grade_f1 = int(row_f1["grade"])
                grades_list.append(grade_f1)
                
        mean_value = statistics.mean(grades_list)
        min_value = min(grades_list)
        max_value = max(grades_list)
        median_value = statistics.median(grades_list)
        stdev_value = statistics.stdev(grades_list)
        
        writer_info.writerow([
            subject,
            mean_value,
            min_value,
            max_value,
            median_value,
            stdev_value
        ])