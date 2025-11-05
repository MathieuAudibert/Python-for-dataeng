def analyser_texte(file):
    with open(file, 'r') as f:
        text = f.read()

    words = text.split()
    num_words = len(words)
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)
    word_with_most_e = max(words, key=lambda w: w.lower().count('e'))
    words_without_e = [word for word in words if 'e' not in word.lower()]
    most_frequent_word = max(set(words), key=words.count)
    frequency = words.count(most_frequent_word)

    print(f"mots: {num_words}")
    print(f"long: {longest_word}")
    print(f"court: {shortest_word}")
    print(f"+ de 'e': {word_with_most_e}")
    print(f"sans'e': {', '.join(words_without_e)}")
    print(f"frequent: {most_frequent_word} (frequence: {frequency})")

analyser_texte('15.py')