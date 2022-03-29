from flask import *

app = Flask(__name__)

@app.route("/")
def hey():
    return 'real'

app.run()