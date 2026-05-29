


import csv
from fileinput import filename

from flask import Flask, render_template, request  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route("/display")
def display():
    return render_template("k2.html")

@app.route("/")
def index():
    return "Welcome to the homepage!"

@app.route('/save_data', methods=['Get','Post'])  #explain this # URL '/' to be handled by main() route handler
def main():
    

    role = request.args.get("role")
    inp = request.args.get("inp")
    
    print(role)

    return "ok data received"


if __name__ == '__main__':
    app.run(debug=True)