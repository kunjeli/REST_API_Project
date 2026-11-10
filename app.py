from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Rahul", "course": "BCA"},
    {"id": 2, "name": "Priya", "course": "B.Tech"}
]

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Backend REST API",
        "status": "API is running successfully"
    })

# GET API
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST API
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('course'):
        return jsonify({"error": "Name and course are required"}), 400

    new_student = {
        "id": max([s["id"] for s in students], default=0) + 1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(debug=True)