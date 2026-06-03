from flask import Flask
app = Flask(__name__) #It creates the Flask application object and uses __name__ to help Flask locate resources such as templates and static files.
students = [
    {
        "name":"Deva",
        "age":"20"
    }
]
@app.route("/")
 #It maps a URL endpoint to a Python function. When a client requests that URL, Flask executes the associated function and returns its response.
 #This is called a decorator. Flask internally does something similar to: app.route("/")(home)
 #Register home() for the URL "/"
def home():
    return "Hello from API"
@app.route("/students")
def get_students():
    return students
#does not work in browsers
@app.route("/students",methods=["POST"])
def create_students():
    data=request.json
    students.append(data)
    return students
app.run(debug=True) #It starts the Flask development server and enables automatic reloading and detailed error messages.