import json


data_base={"hostname":"fibonacci.com","ip":"127.0.0.1","as_ip":"127.0.0.1","as_port":53533}
data_string=json.dumps(data_base)
with open("packet_start.json","w") as file:
    file.write(data_string)