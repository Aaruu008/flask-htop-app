from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/')
def htop_info():
    name = "Aryan Chauhan"  # Replace with your name
    username = getpass.getuser()

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Top command
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], universal_newlines=True)
    except Exception as e:
        top_output = str(e)

    return f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
