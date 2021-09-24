from flask import Flask
import socket

node = Flask(__name__)


@node.route('/', methods=['GET'])
def index():
#     return f"This is QYTAKS:{socket.gethostname()}, My IP is {socket.gethostbyname(socket.gethostname())}"
    return_str=f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Azure CDN Test Kylo</title>
        </head>
        <body>
        <img src="/static/qytanglogo.png"/>
        <h3>This is KyloAKS:{socket.gethostname()}, My IP is {socket.gethostbyname(socket.gethostname())}</h3>
        </body>
        </html>"""
    return return_str

@node.route('/CKTY', methods=['GET'])
def CKTY():
    return_str=f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>CK&TY livehouse</title>
        </head>
        <body>
        <h3>CKTY Forever</h3>
        </body>
        </html>"""
    return return_str
    
if __name__ == "__main__":
    node.run(host='0.0.0.0', port=80)
