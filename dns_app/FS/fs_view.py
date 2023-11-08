from flask import Flask, render_template, request
import json
import time
import socket
app = Flask(__name__)

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
@app.route('/register', methods=['PUT'])
def register():
    print(request.json)
    content=request.json
    name=content["hostname"]
    value=content["ip"]
    as_ip=content["as_ip"]
    as_port=content["as_port"]
    packet=f"TYPE=A\nNAME={name}\nVALUE={value}\nTTL={time.time()}"
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(packet.encode(),(as_ip,as_port))
    return "OK", 201
@app.route("/fibonacci")
def fib():
    x=request.args.get('X', type=int)
    print(x)
    if x is None:
        return "bad x",400
    return str(recur_fibo(x)),200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)