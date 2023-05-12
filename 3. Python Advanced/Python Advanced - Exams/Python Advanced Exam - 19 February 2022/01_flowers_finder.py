from collections import deque

vowels = deque(input().split())
consonants = input().split()

words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

found = False
while vowels and consonants:
    vowel, consonant = vowels.popleft(), consonants.pop()

    for word in words.keys():
        if vowel in words[word]:
            words[word] = words[word].replace(vowel, "")
        if consonant in words[word]:
            words[word] = words[word].replace(consonant, "")

        if len(words[word]) == 0:
            print(f"Word found: {word}")
            found = True
            break

    if found:
        break

if not found:
    print(f"Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join([v for v in vowels])}")
if consonants:
    print(f"Consonants left: {' '.join([c for c in consonants])}")