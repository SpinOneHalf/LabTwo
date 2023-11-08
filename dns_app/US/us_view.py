import requests
from flask import Flask,request
import socket
app = Flask(__name__)


@app.route('/fibonacci',methods=['GET'])
def fibonacci():
    host_name = request.args.get('hostname', type=str)
    fs_port = request.args.get('fs_port', type=int)
    x=request.args.get("number",type=int)
    as_ip=request.args.get("as_ip",type=str)
    as_port=request.args.get("as_port",type=int)
    if host_name is None or fs_port is None or x is None:
        return "host or fs port bad",400
    if as_ip is None or as_port is None:
        return "as_ip and as_port bad",400
    #Get IP address of Fib server
    packet2 = f"TYPE=A\nNAME={host_name}"
    sock=socket.socket(socket.AF_INET,socket.AF_INET)
    sock.sendto(packet2.encode(),(as_ip,as_port))
    responds=sock.recv(1024)
    chunked=responds.decode().split("\n")
    ipstring=chunked[2]
    ip_fs=ipstring.split("=")[-1]
    url=f"http://{ip_fs}:{fs_port}/fibonacci?X={x}"
    r=requests.get(url)
    #Ask for fib!
    return f"OK:{int(r.content)}",200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)