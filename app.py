import os
import signal
import platform
from flask import Flask, render_template
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    buzz = generator.generate_buzz()
    machine = platform.uname()
    machine_text = "INFO system:"+machine.system+" node:"+machine.node+" relase:"+machine.release+" version:"+\
                   machine.version+" machine:"+machine.machine+" processor:"+machine.processor
    return render_template('index.html', buzz=buzz, machine=machine_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))