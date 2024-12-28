from flask import Flask, request, jsonify
from flask_cors import CORS
from Main import generate_password

# Initialize the Flask app and enable CORS for cross-origin requests
app = Flask(__name__)
CORS(app)


@app.route("/submit", methods=["POST"])
def get_input():
    data = request.json.get("data")  # Extract the 'data' field from the request body
    amount_characters = int(data)  # Convert the input to an integer (number of characters)
    password = generate_password(amount_characters)  # Generate a password using the imported function
    return jsonify(
        {"message": f"Your generated password: {password}"})  # Return the generated password in a JSON response


if __name__ == "__main__":
    app.run()
