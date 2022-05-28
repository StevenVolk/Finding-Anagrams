# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) != len(anagram):
        return False

    char_to_check = anagram

    for char in word:
        if char not in char_to_check:
            return False
        char_to_check.replace(char, "")
    return True

#print(find_anagram("hello", "check"))
#print(find_anagram("below", "elbow"))
#print(find_anagram("hello", "helo"))