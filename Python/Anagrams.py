from collections import Counter

def anagram_check(initial_word, word):
    if len(initial_word) != len(word):
        return False
    return sorted(initial_word.lower()) == sorted(word.lower())

print(anagram_check("Python", "Typhon"))

def anagram_check(initial_word, word):
    
    clean1 = ''.join(c.lower() for c in initial_word if c.isalpha())
    clean2 = ''.join(c.lower() for c in word if c.isalpha())

    return Counter(clean1) == Counter(clean2)

print(anagram_check("Dirty room", "Dormitory"))

user_input = input("Enter a word: ")
library = ['python','typhon','sunny','windy']

for word in library:
    if sorted(user_input) == sorted(word):
        print(word)