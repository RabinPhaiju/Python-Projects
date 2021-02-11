1.  a is b
    - id(a)==id(b)
2.  a is b

    - a = 22222
    - b = 22222
    - print(a is b)
      - true in vs code
      - false in cmd

3.  Points to same object memory
    - temp = 20
    - temp2 = 20
    - print(temp == temp2) => true
    - print(temp is temp2) => true
4.  Differnce between is and ==
    - a = [1, 2, 3]
    - b = [1, 2, 3]
    - print(a == b) => true
    - print( a is b) => false
5.  Id of integer
    a = 10
    b = a
    a is b => true
    a = 11
    a is b => false
6.  Id of string
    - a = 'hello'
    - b = 'bye'
    - b += a
    - a is b => false
7.  Id reassign int
    - on_create = a
    - a = 20 # re-assigning variable
    - on_change = a
    - print(on_create is on_change) => false
8.  Id reassign list
    - a = [1,2,3]
    - on_create = a
    - a = [3,4,5] # re-assiging variable
    - on_change = a
    - print(on_create is on_change) => false
9.  list
    - eg_list = [0,1,2,3,4]
    - eg_list2 = [4,1,2,0,3]
    - print(eg_list == eg_list2) => false
10. set
    - eg_set = {'name', 'age', 'college'}
    - eg_set2 = {'age', 'college', 'name'}
    - print(eg_set == eg_set2) => true
