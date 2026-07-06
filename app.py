from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users[user_id]
    return jsonify(user)


if __name__ == "__main__":
    app.run(debug=True)
