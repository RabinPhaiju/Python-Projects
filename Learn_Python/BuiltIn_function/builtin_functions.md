1.  use space over tabs (4 space = 1 indentdation)
2.  bin(x)
    - convert an integer number to a binary string
      - hex(255)
      - oct(8)
3.  @classmethod
    - The @classmethod form is a function decorator
4.  print(eval('2+1'))
5.  kwargs
6.  Enumerate
    - list(enumerate(list, start=1))
7.  filter(function, iterable)

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

8.  float('+1.23')
9.  Format
    - print('{2}, {1}, {0}'.format('a', 'b', 'c'))
    - print('{2}, {1}, {0}'.format(\*'abc')) # unpacking argument sequence
10. Frozen ->immutable
    - vowels = ('a', 'e', 'i', 'o', 'u')
    - frozenset(vowels)
11. map(func, ('apple', 'banana', 'cherry'))
12. list.reverse()
    - reversed_list = systems[::-1]
13. Slice
    - The slice() function returns a slice object that can use used to slice strings, lists, tuple etc.
    - slice(start, stop, step)
    - py_string = 'Python'
    - print(py_string[1:5:2])
