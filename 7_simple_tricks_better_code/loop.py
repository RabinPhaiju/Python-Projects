needle = 'd'
haystack = ['a', 'b', 'c']

for letter in haystack:
    if needle in haystack:
        print('Found')
        break
else:
    print('not found in list')


# ---------------- join---------------
Delimiter = ','
print(Delimiter.join(haystack))