text = "Communicative "
word = text.casefold()
def duplicate(word):
    for x in word:
        if word.count(x) == 1:
            return True
        else:
            return False

print(duplicate(word))