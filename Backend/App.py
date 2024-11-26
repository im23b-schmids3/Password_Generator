from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/submit', methods=['POST'])
def get_input():
    data = request.json.get('data')
    response = f'You have succsesfully submitted: {data}'
    return jsonify({"message": response})


if __name__ == '__main__':
    app.run()