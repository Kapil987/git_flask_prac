from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, this is a flask class</p>"

@app.route("/abc")
def abc_path():
    return "<p>i have added an abc path 345</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
