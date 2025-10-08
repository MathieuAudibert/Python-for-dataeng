def sort_distinct_words():
    phrase = input("Phrase: ")
    words = phrase.split()
    sorted_words = sorted(words, key=lambda w: (len(w), w))
    print(sorted_words)
sort_distinct_words()

