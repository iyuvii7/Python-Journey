import random
import webbrowser
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

# --- PASSWORD GENERATION LOGIC ---
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(l, s, n):
    password_list = []
    password_list.extend(random.choices(letters, k=l))
    password_list.extend(random.choices(symbols, k=s))
    password_list.extend(random.choices(numbers, k=n))
    random.shuffle(password_list)
    return "".join(password_list)

# --- WEB SERVER DESIGN ---
# Notice double curly braces {{ }} around CSS so Python .format() ignores them
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>PyPassword Generator v2.0</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ background-color: #121214; color: #E2E2E2; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .card {{ background-color: #1A1A24; padding: 30px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.5); border: 1px solid #00ADB5; width: 360px; text-align: center; }}
        h2 {{ color: #00ADB5; margin-bottom: 25px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }}
        .slider-group {{ margin-bottom: 20px; text-align: left; }}
        label {{ display: block; margin-bottom: 8px; font-size: 14px; color: #A0A0AA; }}
        input[type=range] {{ width: 100%; accent-color: #00ADB5; background: #121214; height: 6px; border-radius: 3px; outline: none; }}
        .slider-val {{ float: right; color: #00ADB5; font-weight: bold; }}
        button {{ background-color: #00ADB5; color: #121214; border: none; padding: 12px 20px; font-size: 16px; font-weight: bold; border-radius: 6px; cursor: pointer; width: 100%; margin-top: 15px; transition: 0.2s; }}
        button:hover {{ background-color: #00FFFF; box-shadow: 0 0 10px rgba(0,255,255,0.5); }}
        .result-box {{ margin-top: 25px; background: #121214; padding: 12px; border-radius: 6px; border: 1px dashed #444; font-family: 'Courier New', Courier, monospace; font-size: 18px; color: #00FFFF; word-break: break-all; min-height: 24px; position: relative; cursor: pointer; }}
        .result-box:hover::after {{ content: 'Click to Copy'; position: absolute; right: 10px; top: 12px; font-size: 11px; color: #666; font-family: sans-serif; }}
    </style>
</head>
<body>
    <div class="card">
        <h2>Password Generator</h2>
        <form action="/" method="GET">
            <div class="slider-group">
                <label>Letters: <span class="slider-val" id="l_val">{l_val}</span></label>
                <input type="range" name="l" min="0" max="20" value="{l_val}" oninput="document.getElementById('l_val').innerText=this.value">
            </div>
            <div class="slider-group">
                <label>Symbols: <span class="slider-val" id="s_val">{s_val}</span></label>
                <input type="range" name="s" min="0" max="20" value="{s_val}" oninput="document.getElementById('s_val').innerText=this.value">
            </div>
            <div class="slider-group">
                <label>Numbers: <span class="slider-val" id="n_val">{n_val}</span></label>
                <input type="range" name="n" min="0" max="20" value="{n_val}" oninput="document.getElementById('n_val').innerText=this.value">
            </div>
            <button type="submit">Generate Password</button>
        </form>
        <div class="result-box" onclick="navigator.clipboard.writeText(this.innerText); alert('Copied to clipboard! 📋');">{pwd}</div>
    </div>
</body>
</html>
"""

class PasswordServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        params = urlparse.parse_qs(parsed_path.query)
        
        # Read user values or fall back to defaults
        l = int(params.get('l', [8])[0])
        s = int(params.get('s', [4])[0])
        n = int(params.get('n', [4])[0])
        
        pwd = generate_password(l, s, n) if parsed_path.query else "Move sliders & click generate"
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_TEMPLATE.format(l_val=l, s_val=s, n_val=n, pwd=pwd).encode())

    def log_message(self, format, *args):
        return # Keeps terminal logs clean

def open_browser():
    webbrowser.open("http://127.0.0.1:8080")

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8080), PasswordServer)
    print("Opening PyPassword UI in your browser at http://127.0.0.1:8080")
    threading.Thread(target=open_browser).start()
    server.serve_forever()
