string = "eDaBiT"
r = []
def capital_letter(string,r):
    for word in string:
        if word == word.upper():
            r.append(string.index(word))
    return r
print(capital_letter(string,r))
