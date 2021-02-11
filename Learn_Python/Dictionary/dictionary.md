# dict has unique key
## key or value or dict can be float ,int, list, tuple etc
# unordered
1. create

- dict1 = {
  "name":"rabin",
  "age":9
  }

2. create/clear dict
   dict2 = {}

3. add/update dict
   dict2['name']='rabin'

4. loop dict

   - for key in dict1:
     - print(key)
     - print(dict1[key])
   - for k, v in dict1.items():
     - print(k, v)

5. get function

   - x = [
     {"name":"ram","sem":6,"name": "rabin"},
     {"name":"shyam","sem":6},
     {"name":"hari","sem":6},
     {"name":"xyz","sem":6},
     {"name":"rabin","sem":6}
     ]

   - print([i.get('name') for i in x])

6. ## Nesting list and dict
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
7. dictionary comprehension
   - {x: x\*\*2 for x in (2, 4, 6)}

8. dict.item()
  - for key,value in y.items():
  -  print(f"{key}={value}")

9. dict.keys():
  - return the list of keys in dict