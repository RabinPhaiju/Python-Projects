import json

persons  = '''
{
    "person":[
        {
            "name": "rabin",
            "age":  25
        },
        {
            "name": "sabin",
            "age": 20
        }
    ]
}
'''

data = json.loads(persons)

for person in data['person']:
    del person['age']


new_string = json.dumps(data, indent=2)
print(new_string)


