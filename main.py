from flask import *

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def loginpage():
    return render_template("loginpage.html")

@app.route("/register")
def registerpage():
    return "register page"

if __name__ == "__main__":
    app.run(debug=True)