word = "hello world"
word2 = ""

def duplicate(word, word2):
    for alp in word:
        word2 += alp*2
    return word2

print(duplicate(word,word2))