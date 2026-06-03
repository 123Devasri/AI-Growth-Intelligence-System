from flask import Flask
app = Flask(__name__) #It creates the Flask application object and uses __name__ to help Flask locate resources such as templates and static files.
@app.route("/")
 #It maps a URL endpoint to a Python function. When a client requests that URL, Flask executes the associated function and returns its response.
 #This is called a decorator. Flask internally does something similar to: app.route("/")(home)
 #Register home() for the URL "/"
def home():
    return "Hello from API"
@app.route("/about")
def about():
    return "about page"
app.run(debug=True) #It starts the Flask development server and enables automatic reloading and detailed error messages.