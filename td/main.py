import math
from collections import Counter

def sort_distinct_words():
    phrase = input("Phrase: ")
    words = phrase.split()
    sorted_words = sorted(words, key=lambda w: (len(w), w))
    print(sorted_words)
#sort_distinct_words()

def clean_list(L):
    for x in L[:]:
        if not isinstance(x, int) and not isinstance(x, str) and not isinstance(x, float):
            L.remove(x)
        elif isinstance(x, str):
            if not x.isdigit():
                L.remove(x)
            else:
                L[L.index(x)] = int(x)
        elif isinstance(x, float):
            L[L.index(x)] = math.floor(x)
    print(L) 
L = [12, "15", None, "abc", 8, "20", 3.5, "NaN"]
#clean_list(L)

def perfect_number():
    perfect = []  
    for n in range(1, 10000):
        somme = sum(i for i in range(1, n) if n % i == 0)
        if somme == n:
            perfect.append(n)
    print(perfect)
#perfect_number()

def scan_text(text):
    word_count = len(text.split())
    frequent_words = sorted(set(text.split()), key=text.split().count, reverse=True)
    moyenne = sum(len(mot) for mot in text.split()) / len(text.split())
    
    frequent_letter = {}
    for char in text:
        if char.isalpha():
            if char in frequent_letter:
                frequent_letter[char] += 1
            else:
                frequent_letter[char] = 1
    letters = {k: v for k, v in sorted(frequent_letter.items(), key=lambda item: item[1], reverse=True)}
    print(word_count, "\n", frequent_words[:10], "\n", moyenne, "\n", letters)
#scan_text("je m'appelle mathieu et je suis ingénieur. Roméo est un ingenieur aussi qui travaille a imagino en tant que swe r&dje m'appelle mathieu et je suis ingénieurje m'appelle mathieu et je suis ingénieur")

def trouver_sous_ensemble(L, S):
    ensemble = []
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[i] + L[j] == S:
                ensemble.append([L[i], L[j]])
    print(ensemble)
trouver_sous_ensemble([2, 3, 5, 7], 10)