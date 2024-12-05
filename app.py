from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/goodbye")
def goodbye():
    return "Good Bye"


@app.route("/user/<name>")
def hi(name):
    return f"Hi,{name}!"


@app.route("/about/<name>")
def about(name):
    return f"{name}'s profile"


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=8000, debug=True)
