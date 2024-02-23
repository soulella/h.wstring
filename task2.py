def count_characters(lst):
    res = 0
    for x in lst:
        res += len(x)
    return res


print(count_characters([
  "###",
  "###",
  "###"
]))