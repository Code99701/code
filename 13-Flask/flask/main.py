from flask import Flask, request, jsonify, render_template
'''
It creates an instance of the Flask class, 
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("/")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
  app.run(debug=True)
