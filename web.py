from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
<title>My Web Server</title>
</head>
<body>
    <center>
    <table border="10" cellpadding="30">
        <caption><h3>MY SYSTEM CONFIGURATION</h3></caption>
        <tr bgcolor="yellow" style="color:black;">
          <th bgcolor="antiquewhite">S.no</th><th>Item</th><th>Value</th>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
          <td bgcolor="yellow" style="color:black;">1</td><td>OS Name</td><td>Microsoft Windows 10 Pro</td>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
          <td bgcolor="yellow" style="color:black;">2</td><td>System Manufacturer</td><td>HP</td>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
          <td bgcolor="yellow" style="color:black;">3</td><td>System Model</td><td>EliteBook 840 G3</td>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
          <td bgcolor="yellow" style="color:black;">4</td><td>RAM</td><td>8 GB DDR4</td>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
          <td bgcolor="yellow" style="color:black;">5</td><td>Processor</td><td>Intel i5 6th Gen</td>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
          <td bgcolor="yellow" style="color:black;">6</td><td>SSD</td><td>256 GB</td>
        </tr>
    </table>
    </center>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

# Fixed: Removed space in IP address string
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running on port 8000...")
httpd.serve_forever()
