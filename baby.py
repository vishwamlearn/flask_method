from os import name
from flask import Flask,render_template,request,redirect
from flask.helpers import url_for

app=Flask(__name__)

@app.route("/")
def baby():
    return render_template("welcome.html", message='Kuhu ka vishwam', items=['pudina', 'dhaniya','aam'])


@app.route("/hi/<name>")
def yoyo(name):
    return '<h1>I Love you {} :)</h1>'.format(name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("baby.html"),404

@app.route("/food_accepted")
def food_found(): 
    return "<h1> 'Food acepted  baby' </h1>"

@ app.route('/today_menu', methods=["GET","POST"])
def menu():
    if request.method=="POST":
        return redirect(url_for("food_found"))
    else:
        return render_template("menu.html")
if __name__ == '__main__':
    app.run(debug=True)