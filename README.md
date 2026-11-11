# EX01 Developing a Simple Webserver
## Date:11/11/26
## Reg no:26012370

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial;
            background-color: #fff7ed;
            text-align: center;
            padding: 10px;
        }

        h1 {
            color: #9a3412;
        }

        .box {
            background-color: white;
            width: 75%;
            margin: 13px auto;
            padding: 8px;
            border-left: 6px solid #f59e0b;
            border-radius: 8px;
        }

        h3 {
            color: #c2410c;
        }

        p {
            color: #444;
            font-size: 16px;
        }

        footer {
            color: #9a3412;
            margin-top: 18px;
        }
    </style>
</head>

<body>

    <h1>🌐 TCP/IP Protocol Suite</h1>
    <p>Four Layers and Their Protocols</p>

    <div class="box">
        <h3>1. Application Layer</h3>
        <p>HTTP | HTTPS | FTP | SMTP | DNS | DHCP | Telnet</p>
    </div>

    <div class="box">
        <h3>2. Transport Layer</h3>
        <p>TCP | UDP</p>
    </div>

    <div class="box">
        <h3>3. Internet Layer</h3>
        <p>IP | ICMP | IGMP | ARP</p>
    </div>

    <div class="box">
        <h3>4. Network Access Layer</h3>
        <p>Ethernet | Wi-Fi | PPP</p>
    </div>

    <footer>
        <b>Communication Through Networks</b>
    </footer>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',420)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~


## OUTPUT:
![alt text](<Screenshot 2026-11-03 135837.png>)

![alt text](<Screenshot 2026-11-03 135923.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

