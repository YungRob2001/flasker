from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

#def index():
#    return "<h1>hello world</h1>"
def index():
    first_name="john"
    favorite_icecream=["vanilla","cocholate","fruits"]
    stuff="this is bold text"
    return  render_template("index.html",
                            first_name=first_name,
                            stuff=stuff,
                            favorite_icecream=favorite_icecream)


@app.route('/user/<name>')

def user(name):
    return  render_template("user.html",name=name)

@app.errorhandler(404)
def page_nout_found(e):
    return  render_template("404.html"),404

@app.errorhandler(500)
def page_nout_found(e):
    return  render_template("500.html"),505


