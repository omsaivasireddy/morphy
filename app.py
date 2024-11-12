from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Om Sai Vasireddy"

    username = "omsai"

    # Get server time in IST
    ist_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Run the `top` command and capture output
    top_output = subprocess.getoutput("top -bn 1")

    # Format the response
    response = f"""
    Name: {name}<br>
    Username: {username}<br>
    Server Time (IST): {ist_time}<br><br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)