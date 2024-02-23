society_name = ["Adam", "Sarah", "Malcolm"]
first = []

def find_secret(name, lst):
    for x in name:
        lst.append(x[0])
        lst.sort()
    j = "".join(lst)
    return j
print(find_secret(society_name,first))