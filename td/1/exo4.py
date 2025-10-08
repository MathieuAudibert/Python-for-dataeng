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
scan_text("je m'appelle mathieu et je suis ingénieur. Roméo est un ingenieur aussi qui travaille a imagino en tant que swe r&dje m'appelle mathieu et je suis ingénieurje m'appelle mathieu et je suis ingénieur")