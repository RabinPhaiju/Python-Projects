# range(start, end, step)

1. for i in range(5):

2. enumerate

   - persons = ['ram', 'shyam', 'hari', 'tari']
   - for index, value in enumerate(persons):
     - print(index, value)
   - for i in enumerate(persons):
     - print(i)

3. Touple unpacking

   - touple_list = [(1,2), (3,4), (5,6)]
   - for (a,b) in touple_list:
     - print(a,"\n",b)

4. Undifined variable loop
   - for \_ in range(10):
     - print('!cool')
5. zip -> loop multiple list at once

   - for item in zip(list1, list2, list3):
     - print(item)

6. for else -> else run after loop

   - for i in range(10):
     - print(i)
   - else:
     - print('fully executed')

7. Negative indexing

   - print(list(range(10, 5, -1)))
   - for i in range(10,5,-1):
     - print(i)

8. Nested Loop

   - mylist = [x\*y for x in [2, 4, 6] for y in [1, 10, 100]]
   - [[j for j in range(1, 3)] for i in range(4)]
   - [list(range(1, 3)) for i in range(4)]
   - {i: {j: j for j in range(2)} for i in range(10)}
   - [{j: j for j in range(2)} for i in range(10)]
