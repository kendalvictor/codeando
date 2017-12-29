import re

result_store = ["abc", "aBc", "ABC", "abC", "ADb", "aBD"]


patron_minus_mayus = re.compile("{0}".format('abc'), re.I)



for row in result_store:
    print patron_minus_mayus.search(row)


conjunto = {'a', 'b'}

print(conjunto)
conjunto.update(None)
print(conjunto)


