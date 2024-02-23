word = "Ihave never seen a thin person drinking Diet Coke"
vowels = "aouie"
str = ""
def remove_vowel(word,vowels,str):
    for x in word:
        if x not in vowels:
            str += x
    return str

print(remove_vowel(word,vowels,str))