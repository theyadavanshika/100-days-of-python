from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function(function):
        pass

def make_emphasis(function):
    def wrapper_function(function):
        pass

def make_underlined(function):
    def wrapper_function(function):
        pass

@app.route("/")
def hello_world():
    return "<h1 style=text-align:center> Hello, In the Cat World! </h1>" \
    "<p>I'm just a cute cat</p> " \
    "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTdhYzFvMnFmZDB2ZG82OHdnc3U3Znhxc3ViN2dhZzNzcHpvaWJ4aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3z3Jqt42yS104gRc5c/giphy.gif' width=200> "

@app.route("/Bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hey there {name}!<br>You're {number} years old"

if __name__ == "__main__":
    app.run(port=5001, debug=True)