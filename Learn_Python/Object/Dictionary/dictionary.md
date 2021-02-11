# dict has unique key unordered -> no index

    - key value pair
    - the keys and values can be of any type.
    - dictionary is indexed through the keys.
    - same key cannot be assigned. which is replace/update thre prev
    - key or value or dict can be float ,int, list, tuple etc

1. create

   - empty_lsit={}
   - empty_list = dict()
   - dict1 = {
     "name":"rabin",
     "age":9
     }

2. access the keys and value

   - dict.keys()
   - dict.values()
   - dict['key']
   - dict.get('age', 'Not found')

3. create/clear dict
   dict2 = {}

4. add/update dict

   - dict2['name']='rabin'
   - dict2.update(dict1)

5. delete a key,value

   - del dict['age']

6. check key exist

   - 'name' in eg_dict

7. loop dict

   - for key in dict1:
     - print(key)
     - print(dict1[key])
   - for k, v in dict1.items():
     - print(k, v)

8. get function -> if we access key not available -> returns None or default value

   - x = [
     {"name":"ram","sem":6,"name": "rabin"},
     {"name":"shyam","sem":6},
     {"name":"hari","sem":6},
     {"name":"xyz","sem":6},
     {"name":"rabin","sem":6}
     ]

   - print([i.get('name') for i in x])

9. ## Nesting list and dict
   person ={
   "name":['rabin','ram'],
   "school":{
   - "school1":"boston",
     "school2:"yung"
     "france":{
     - "cities_visited":['paris','dijon'],
       "total":12
       }
       }
       }
10. dictionary comprehension

    - {x: x\*\*2 for x in (2, 4, 6)}
    - {i: i\*\*2 for i in range(10) if i % 2 == 0}
    - {i: i\*\*2 for i in range(10) if i % 2 == 0 if i > 5}
    - {i: ('even' if i % 2 == 0 else 'odd') for i in range(10)}

11. dict.item()

    - for key,value in y.items():
    - print(f"{key}={value}")

12. dict.keys():

    - return the list of keys in dict

13. Convert list to dic

    - ['hello','bye','ll']
    - print({i: v for i, v in enumerate(eg_list, 1)})
