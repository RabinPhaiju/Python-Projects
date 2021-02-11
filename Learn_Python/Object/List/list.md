1. List

   - empty list = []
     - list()
   - eg_list2 = [1, 2, 3, [200, 300, [100, [400, [18, [19]]]]]]
     - eg_list2[3][-1][1][1][1][0] =>19

2. check element in list

   - print(3 in list)

3. check the list contains elements of another list

   - all(item in List1 for item in List2)
   - any(item in List1 for item in List2)

4. List methods

   - list.append() :- add at the end of the list

     - a[len(a):] = [x].

   - list.pop([i])

     - Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes the last

   - list.extend(list1)

     - a[len(a):] = iterable

   - list.insert(0, x)

     - a.insert(len(a), x) is equivalent to a.append(x).
     - a.insert(1,x) -> insert at position 1

   - list.remove(x)

     - Remove the first item from the list whose value is equal to x

   - list.clear()

     - Remove all items from the list
     - del a[:].

   - list.index(x[, start[, end]])

   - list.count(x)

     - Return the number of times x appears in the list.

   - list.sort(\*, key=None, reverse=False)
   - list.reverse()

     - print(days[::-1])

   - list.copy()
     - Return a shallow copy of the list. Equivalent to a[:]

5. Remove duplicate values from list

   - list(set([1,1,2,4,5,5,6,7]))

6. List comprehensions

   - syntax
     - [item for item in iterable]
     - [x for x in iterable if_condition]
     - [x if_con else_con for x in iterable]
   - squares = list(map(lambda x: x\*\*2, range(10)))
   - squares = [x**2 for x in range(10) if x%2==0]
   - [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
   - [(x, x**2) for x in range(6)]
   - [abs(x) for x in vec]
   - freshfruit = [' banana', ' loganberry ', 'passion fruit ']
   - [weapon.strip() for weapon in freshfruit]

7. Nested list comprehension

   - matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
     - [[row[i] for row in matrix] for i in range(4)] # transpose
     - list(zip(\*matrix))

8. list unpacking

   - a,b,c=[1,2,3]
   - a,b,c,\*other = [1, 2, 3, 4, 5, 7, 8]
