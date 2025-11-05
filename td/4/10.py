import csv
import random

def charger_questions(fichier_csv):
    questions = []
    with open(fichier_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            questions.append({
                'question': row['question'],
                'reponses': [row['rep1'], row['rep2'], row['rep3']],
                'bonne_reponse': int(row['num_bonne_reponse'])
            })
    return questions

def poser_question(question):
    print("\n" + question['question'])
    for i, rep in enumerate(question['reponses'], start=1):
        print(f"{i}. {rep}")
    while True:
        try:
            reponse = int(input("Votre réponse (1-3) : "))
            if 1 <= reponse <= 3:
                return reponse
            else:
                print("Veuillez entrer un nombre entre 1 et 3.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def qcm(fichier_csv):
    questions = charger_questions(fichier_csv)
    questions_a_poser = random.sample(questions, 5)
    score = 0

    for question in questions_a_poser:
        reponse = poser_question(question)
        if reponse == question['bonne_reponse']:
            print("Bonne réponse !")
            score += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse était {question['bonne_reponse']}.")

    print(f"\nscore : {score}/5")

if __name__ == "__main__":
    fichier_csv = "questions.csv"
    qcm(fichier_csv)