1. Mutable

   - which can change value without changing memory address
   - list, dict, set,
   - mutable changes in same address dont need to return from function

   1. List
      - eg_list = [1, 2, 3]
      - print(eg_list) => same address
      - eg_list.append(2)
      - print(id(eg_list)) => same address

2. Imutable
   1. Integer
      - a = 10
      - b = a
      - b = 11
      - a is b => false
   2. String
      - eg_str2[1] = 'a' # not allowed
      - a = 'ram'
      - a += ' shyam'
      - diff address
