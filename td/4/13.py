import os
import json
import re

def build_inverted_index(documents_dir):
    inverted_index = {}
    for filename in os.listdir(documents_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(documents_dir, filename)
            with open(filepath, encoding='utf-8') as f:
                text = f.read().lower()
                words = re.findall(r'\b\w+\b', text)
                for word in set(words):
                    inverted_index.setdefault(word, []).append(filename)
    return inverted_index

def save_index(index, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

def rechercher(mot, index_path='index.json'):
    mot = mot.lower()
    with open(index_path, encoding='utf-8') as f:
        index = json.load(f)
    return index.get(mot, [])

if __name__ == "__main__":
    documents_dir = 'documents'
    index = build_inverted_index(documents_dir)
    save_index(index, 'index.json')
    # print(rechercher('entreprise'))