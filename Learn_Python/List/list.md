1. List

   - list.append() :- add at the end of the list
     - a[len(a):] = [x].
   - list.extend(list1)
     - a[len(a):] = iterable
   - list.insert(0, x)
     - a.insert(len(a), x) is equivalent to a.append(x).
   - list.remove(x)
     - Remove the first item from the list whose value is equal to x
   - list.pop([i])
     - Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes the last
   - list.clear()
     - Remove all items from the list
     - del a[:].
   - list.index(x[, start[, end]])
   - list.count(x)
     - Return the number of times x appears in the list.
   - list.sort(\*, key=None, reverse=False)
   - list.reverse()
   - list.copy()
     - Return a shallow copy of the list. Equivalent to a[:]

2. Remove duplicate values from list

   - list(set([1,1,2,4,5,5,6,7]))

3. List comprehensions

   - squares = list(map(lambda x: x\*\*2, range(10)))
   - squares = [x**2 for x in range(10) if x%2==0]
   - [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
   - [(x, x**2) for x in range(6)]
   - [abs(x) for x in vec]
   - > > > freshfruit = [' banana', ' loganberry ', 'passion fruit ']
   - > > > [weapon.strip() for weapon in freshfruit]

4. Nested list comprehension

   - matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
     - [[row[i] for row in matrix] for i in range(4)] # transpose
     - list(zip(\*matrix))

5. Using list as queue

   > > > from collections import deque
   > > > queue = deque(["Eric", "John", "Michael"])
   > > > queue.append("Terry") # Terry arrives
   > > > queue.append("Graham") # Graham arrives
   > > > queue.popleft() # The first to arrive now leaves
   > > > 'Eric'
   > > > queue.popleft() # The second to arrive now leaves
   > > > 'John'
   > > > queue # Remaining queue in order of arrival
   > > > deque(['Michael', 'Terry', 'Graham'])
