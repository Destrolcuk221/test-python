import json
pythonDictionary = {"nombre":"Python","tipo":"backend" ,"paradigma":"Orientado a Objetos"}
dictionaryToJson = json.dumps(pythonDictionary)

print(dictionaryToJson)