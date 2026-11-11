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