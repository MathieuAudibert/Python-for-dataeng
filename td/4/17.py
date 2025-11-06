import os
import csv
import json
from collections import defaultdict

# 1. 
notes_folder = "notes"

if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)

txt_files = [f for f in os.listdir(notes_folder) if f.endswith('.txt')]

# 2. 
data = []
for file in txt_files:
    with open(os.path.join(notes_folder, file), 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 4:
                data.append({
                    "Nom": parts[0].strip(),
                    "Prénom": parts[1].strip(),
                    "Module": parts[2].strip(),
                    "Note": float(parts[3].strip())
                })

# 3. 
valid_data = []
invalid_data = []
for entry in data:
    if 0 <= entry["Note"] <= 20:
        valid_data.append(entry)
    else:
        invalid_data.append(entry)

# 4. 
with open("notes_invalides.txt", 'w', encoding='utf-8') as f:
    for entry in invalid_data:
        f.write(f"{entry['Nom']}, {entry['Prénom']}, {entry['Module']}, {entry['Note']}\n")

# 5. 

student_averages = defaultdict(list)
for entry in valid_data:
    student = f"{entry['Nom']} {entry['Prénom']}"
    student_averages[student].append(entry["Note"])

student_averages = {student: sum(notes) / len(notes) for student, notes in student_averages.items()}

# 6. 
module_averages = defaultdict(list)
for entry in valid_data:
    module_averages[entry["Module"]].append(entry["Note"])

module_averages = {module: sum(notes) / len(notes) for module, notes in module_averages.items()}

# 7. 
best_student = max(student_averages, key=student_averages.get)
best_average = student_averages[best_student]

# 8. 
with open("resultats.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Prénom", "Moyenne Générale"])
    for student, avg in student_averages.items():
        nom, prenom = student.split()
        writer.writerow([nom, prenom, avg])

# 9. 
with open("rapport_notes.txt", 'w', encoding='utf-8') as f:
    f.write(f"Meilleur étudiant : {best_student} avec une moyenne de {best_average:.2f}\n")
    f.write("Moyennes par module :\n")
    for module, avg in module_averages.items():
        f.write(f"  {module}: {avg:.2f}\n")

# 10. 
results = {
    "student_averages": student_averages,
    "module_averages": module_averages,
    "best_student": {"name": best_student, "average": best_average}
}

with open("resultats.json", 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4, ensure_ascii=False)