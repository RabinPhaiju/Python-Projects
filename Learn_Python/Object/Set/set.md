1. sets

   - mutable
   - set is an unordered collection with no duplicate elements.
   - a = {x for x in 'abracadabra' if x not in 'abc'}

2. empty set

   - a = set()

3. add item in set

   - set.add('text')
   - fruits[0] -> 'set' object is not subscriptable

4. delete from set

   - set.discard('name')

5. get common element from lists

   - list1 = ["ram","shyam",1,2,3,"hari"]
   - list2 = ["shyam",2,3,10]
   - list(set(list1) & set(list2))

6. unordered

   - set have no indexing
   - print({1,2,3}=={2,1,3}) = True

7. methods -> print(dir(set))

   - summer = {'banana', 'watermelon', 'grapes', 'lemon', 'berries'}
   - winter = {'orange', 'banana', 'pineapple', 'lemon', 'kiwi'}
   - spring = {'watermelon', 'grapes'}

   - print('union: ', summer | winter)
   - print('intersection: ', summer & winter)
   - print('difference: ', summer - winter)
   - print('symmetric difference: ', summer ^ winter)

8. Subset
   - print('subset: ', spring <= summer)
   - print(set1.issubset(set2))
     - returns True if spring is subset of summer else False
9. Superset
   - print('superset: ', summer >= spring )
   - print(set1.issuperset(set2))
     - returns True if summer is superset of spring else False
