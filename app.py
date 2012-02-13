from flask import Flask
from nameparts import Name
from json import dumps

app = Flask(__name__)

@app.route("/")
def index():
    n = Name("James Polera")
    return dumps(n.as_dict)

if __name__ == "__main__":
    app.run()
