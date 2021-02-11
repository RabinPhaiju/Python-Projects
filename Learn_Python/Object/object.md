1. Object

   - set
   - list
   - tuple
   - dict
   - frozenset

2. dir()

   - a = [1,2]
   - print(dir(a))
   - displays the methods available for the object

3. id()

   - gives the memory id

4. id in function

   - pass by referrence

5. list in function

   - append in list changes in same memory location

6. Mutable

   - list, set, dict

7. Immutable
   - bool
   - int
   - float
   - tuple
   - str
   - frozenset
8. Type casting

   - eg_list = [1, 2, 3, 4, 1]
   - eg_tuple = tuple(eg_list) => to tuple
   - eg_set = set(eg_list) => to set

9. Mutable list example

   - a = [1,2,4]
   - a.append(5) => address of a is same if append

10. Mutalbe dict example

    - eg_dict = {'name': 'ram', 'college': 'kec'}
    - on_create = eg_dict
    - eg_dict['newkey'] = 'newvalue'
    - on_change = eg_dict
    - print(on_create is on_change) => true

11. Mutable set exaple
    - eg_set = set()
    - print(id(eg_set)) => same id
    - eg_set.add('name')
    - print(id(eg_set)) => same id
    - eg_set.add('height')
    - print(id(eg_set)) => same id
