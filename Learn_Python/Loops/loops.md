1. Loop

   - knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   - for k, v in knights.items():
     - gallahad the pure
     - robin the brave
   - for i, v in enumerate(['tic', 'tac', 'toe']):

2. Loop over two list at same time

   - questions = ['name', 'quest', 'favorite color']
   - answers = ['lancelot', 'the holy grail', 'blue']
   - for q, a in zip(questions, answers):
     - print('What is your {0}? It is {1}.'.format(q, a))

3. reversed loop

   - for i in reversed(range(1, 10, 2)):

4. sorted loop

   - for i in sorted(basket):

5. sorted set with no duplicate

   - for f in sorted(set(basket)):

6. split

   - name = "rabin,sabin,ram"
   - names = name.split(", ")
   - names[0] ->rabin

7. Conversion

   - 1. String to List of Strings
     - sentence.split()
   - 2. String to List of Characters
     - list(word)
   - 3. List of Strings to List of Lists
     - list1=list(map(list,string1))
   - 4. A string consisting of integers to list of integers
     - list1=list(string1.split())

8. sum the list

   - sum([x for x in range(1,10)])
   - [x for x in range(1,10) if x%2==0]

9. FizzBuzz
