from flask import Flask, request, jsonify
'''
It creates an instance of the Flask class, 
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the good Flask App! i am learning flask"

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__ == '__main__':
  app.run(debug=True)
