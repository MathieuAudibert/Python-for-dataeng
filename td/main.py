import math

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