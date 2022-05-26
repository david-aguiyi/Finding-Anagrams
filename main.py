def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    word = word.split()
    word = word.sort()
    anagram = anagram.lower()
    anagram = anagram.split()
    anagram = anagram.sort()
    if word == anagram:
        return True
    else:
        return False

print(find_anagram("Dog", "God"))

