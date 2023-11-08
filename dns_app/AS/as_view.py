import socket
import json
IP="127.0.0.1"
port=53533

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind((IP,port))
with open("names.json","r") as file:
    string=file.read()
    data_base=json.loads(string)
print(data_base)
print(f"listening on ip {IP} port {port}")
while True:
    data,address=sock.recvfrom(1024)
    print(f"recieved message from :{address}")
    chunked=data.decode().split("\n")
    print(len(chunked))
    print(chunked)
    if len(chunked)==2:
        print("GOT A REQUEST FOR IP")
        name = chunked[1].split("=")[-1]
        ip=data_base[name][0]
        tll=data_base[name][1]
        packet=f"TYPE=A\nNAME={name}\nVALUE={ip}\nTTL={tll}"
        sock.sendto(packet.encode(),address)
    elif len(chunked)==4:
        print("REGISTRATION TIME?!?!?")
        name=chunked[1].split("=")[-1]
        ip=chunked[2].split("=")[-1]
        tll=chunked[3].split("=")[-1]
        data_base[name]=(ip,tll)
    open("names.json","w").close()
    data_string = json.dumps(data_base)
    with open("names.json", "w") as file:
        file.write(data_string)
