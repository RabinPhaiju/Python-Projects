from collections import Counter


my_list = [1, 2, 3, 5, 1, 2, 3, 4, 1, 2, 3, 4]

print(Counter(my_list)) # returns dict

my_list1 = 'assdasdfgfasdfa'
print(Counter(my_list1))

my_words = ' how are you i am fine how are you i am fine how are you'
words = my_words.split(' ')
w = Counter(words)
print(w)

print(w.most_common(2))

# common partterns when using the Counter() object
print(sum(w.values()))                 # total of all counts
# w.clear()                              # reest all counts
print(list(w))                          # list unique elements
print(set(w))                           # convert to a set
print(dict(w))                          # convert to a regular dictionary
print(w.items())                        # convert to a list of (elem, cnt) pairs
pair = w.items()
print(Counter(dict(pair)))              # convert from a list of (elem, cnt) pairs

w += Counter()                          # remove zero and negative counts
print(w)
