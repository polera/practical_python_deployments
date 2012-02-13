from flask import Flask, render_template, request
from nameparts import Name
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        try:
            name = request.form['name_to_parse'] or None
            np = Name(name)
            return render_template("index.html",parsed_name=np)
        except KeyError:
            pass
        else:
            np = Name("James Polera")
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)
