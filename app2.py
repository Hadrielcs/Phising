# save as app.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

HOST = "0.0.0.0"
PORT = 8080

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        body{
            font-family: Arial;
            background:#f0f0f0;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
        }
        .box{
            background:white;
            padding:30px;
            border-radius:10px;
            width:300px;
            box-shadow:0 0 10px rgba(0,0,0,0.2);
        }
        h2{
            text-align: center; /* Centers the heading */
            margin-bottom: 20px;
        }
        input{
            width:100%;
            padding:10px;
            margin-top:10px;
            box-sizing: border-box;
        }
        button{
            width:100%;
            padding:10px;
            margin-top:15px;
            background:#007bff;
            color:white;
            border:none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Login Page</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()

        # Parse the form data
        data = parse_qs(post_data)

        # Extract values
        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        # Prints the exact credentials directly to the server terminal
        print("\n--- NEW LOGIN SUBMISSION ---")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print("----------------------------\n")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"<h1>Login received for testing.</h1>")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), MyServer)
    print(f"Server running at http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down.")
        server.server_close()
