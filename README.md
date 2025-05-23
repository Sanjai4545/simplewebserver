# EX01 Developing a Simple Webserver
## Date:

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
```
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

Fixed: Removed space in IP address string
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running on port 8000...")
httpd.serve_forever()

```
## OUTPUT:
![alt text](<Screenshot 2025-05-21 124522.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
