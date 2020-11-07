import json
# Json = Java script object notation
# load -> read/load json dict
# loads -> convert string contain dict to dict
# dump -> write dict to file
# dumps -> convert object/dict to string

# loads the file with json and turns in to dictionary
data = []
with open('file.json', 'r') as f:
    data = json.load(f) # read/load json dict
    # print(type(data))
    print(data[0]['userId'])

    # print(data[0:2])

# changes the dictionary to string
    json_str = json.dumps(data[0])
    # print(type(json_str))
    print(json_str)

# loads the json string and converts to the dictionary
    dict_str = '{"name":"rabin","age":12}'
    print(type(dict_str))
    dict_obj = json.loads(dict_str)
    print(type(dict_obj))


with open('second.json', 'w') as f:
    # json.dump(temp, f)
    json.dump(dict_obj, f, indent=2)




