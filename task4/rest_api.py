from flask import Flask,jsonify, request

app = Flask(__name__)

users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

@app.route('/')
def home():
    return "API is running"

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        return jsonify(users)

    if request.method == 'POST':
        data = request.get_json()
        new_id = max(users.keys()) + 1
        users[new_id] = {"name": data["name"], "email": data["email"]}
        return jsonify({new_id: users[new_id]})

@app.route('/users/<int:user_id>',methods = ['GET','PUT','DELETE'])
def get_or_update_user(user_id):
    if request.method == 'GET':
        user = users.get(user_id)
        if user:
            return jsonify({user_id: user})
        else:
            return jsonify({"error": "User not found"}), 404

    
    if request.method == 'PUT':
        data = request.get_json()
        if user_id in users:
            users[user_id]["name"] = data["name"]
            users[user_id]["email"] = data["email"]
            return jsonify({user_id: users[user_id]})
        else:
            return {"error":"User not found"}, 404

    if request.method == 'DELETE':
        if user_id in users:
            deleted_user = users.pop(user_id)
            return jsonify({"message": f"User {user_id} deleted", "deleted": deleted_user})

        else:
            return {"error": "User not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
