import json
with open('json_file.JSON', 'r') as f:
    json_content = f.read()
    data = json.loads(json_content)
    print(data)
    print(type(data))
    print(data['some_bool'])