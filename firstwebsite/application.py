from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]=True
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/carPics")
def carPics():
    return render_template("carPics.html")

@app.route("/carSearch")
def carSearch():
    return render_template("carSearch.html")
