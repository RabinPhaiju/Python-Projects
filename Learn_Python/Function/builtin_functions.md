1.  use space over tabs (4 space = 1 indentdation)
2.  bin(x)
    - convert an integer number to a binary string
      - hex(255)
      - oct(8)
3.  @classmethod
    - The @classmethod form is a function decorator
4.  count()
    - list.count()
    - tuple.count()
5.  print(eval('2+1'))
6.  kwargs
7.  Enumerate
    - list(enumerate(list, start=1))
8.  filter(function, iterable)

    - letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o'] # function that filters vowels
      def filterVowels(letter):
      vowels = ['a', 'e', 'i', 'o', 'u']

          if(letter in vowels):
              return True
          else:
              return False

      filteredVowels = filter(filterVowels, letters)

      print('The filtered vowels are:')
      for vowel in filteredVowels:
      print(vowel)

9.  float('+1.23')
10. Format
    - print('{2}, {1}, {0}'.format('a', 'b', 'c'))
    - print('{2}, {1}, {0}'.format(\*'abc')) # unpacking argument sequence
11. Frozen ->immutable
    - vowels = ('a', 'e', 'i', 'o', 'u')
    - frozenset(vowels)
12. map(func, ('apple', 'banana', 'cherry'))
13. max(list)
14. min(list)
15. list.reverse()
    - reversed_list = systems[::-1]
16. Slice
    - The slice() function returns a slice object that can use used to slice strings, lists, tuple etc.
    - slice(start, stop, step)
    - py_string = 'Python'
    - print(py_string[1:5:2])
