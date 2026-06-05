from flask import Flask
app = Flask(__name__) #It creates the Flask application object and uses __name__ to help Flask locate resources such as templates and static files.
#CRUD APP
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

@app.route("/students",methods=["GET"])
def get_students():
    return students,200

@app.route("/students/<id:int>",methods=["GET"])
def get_one_student(id):
    for student in students:
        if student["id"]==id:
            return student,200
    return {"error:student not found"},404

#does not work in browsers
@app.route("/students",methods=["POST"])
def create_students():
    data=request.json
    students.append(data)
    return students,201

@app.route("/students/<id:int>",methods=["PUT"])
def update_student(id):
    data=request.json
    for studnent in students:
        if student["id"]==id:
            student["name"]=data["name"]
            return student,200
    return {"Error;Student not found"},404

@app.route("/students/<id:int>",methods=["DELETE"])
def remove_student(id):
    for student in students:
        if student["id"]==id:
            student.remove(student)
            return {"message:student removed successfully"},200
    retrun {"error:student not found"},404
app.run(debug=True) #It starts the Flask development server and enables automatic reloading and detailed error messages.