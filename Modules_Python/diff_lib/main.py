import sys
import difflib


# difflib.context_diff(a, b, fromfile='', tofile='')

from difflib import context_diff
s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guidoo\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
# sys.stdout.writelines(context_diff(s1, s2, fromfile='before.py', tofile='after.py'))


# difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)
from difflib import get_close_matches

kwlist = {'appel': ['ape', 'apple', 'peach', 'puppy'], 'aplle':['ape', 'apple', 'peach', 'puppy']}
print(get_close_matches('apple', kwlist))
