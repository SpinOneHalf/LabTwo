import json


data_base={}
data_string=json.dumps(data_base)
with open("names.json","w") as file:
    file.write(data_string)
