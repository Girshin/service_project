from flask import Flask, request
import os
import socket

app = Flask(__name__)

@app.route('/')
def ip_addr():
    ip_addr = request.remote_addr
    hostname = socket.gethostname()
    return 'Hello! Your IP address is: ' + ip_addr + '  Your hostname: ' + hostname 


port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', debug=True, port=port)
