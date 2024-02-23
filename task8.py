lst = "abcdefg"
def order(lst):
    if sorted(lst)==list(lst):
        return True
    else:
        return False

print(order(lst))
