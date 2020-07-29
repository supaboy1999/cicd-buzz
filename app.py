import os
import signal
import platform
from flask import Flask, render_template, request
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    buzz = generator.generate_buzz()
    title = buzz[:16]
    machine = platform.uname()
    return render_template('index.html', buzz=buzz, machine=machine,title=title)
@app.route('/', methods=['POST'])
def generate_buzz_with_text():
    text = request.form["text"]
    text = text.upper()
    buzz = generator.generate_buzz()
    title = buzz[:16]
    machine = platform.uname()
    return render_template('index.html', buzz=buzz, machine=machine,title=title,text=text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))