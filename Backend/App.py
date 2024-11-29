from flask import Flask, request, jsonify
from flask_cors import CORS
from Main import generate_password

app = Flask(__name__)
CORS(app)


@app.route("/submit", methods=["POST"])
def get_input():
    data = request.json.get("data")
    amount_characters = int(data)
    password = generate_password(amount_characters)
    return jsonify({"message": f"Your generated password: {password}"})


if __name__ == "__main__":
    app.run()
