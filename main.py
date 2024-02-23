def reverser(word):
    a = word[::-1]
    text = a.swapcase()
    return text
print(reverser("Hello World"))