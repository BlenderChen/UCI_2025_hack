from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample suggestions list
SUGGESTIONS = [
    "New York Apartments",
    "Los Angeles Condos",
    "San Francisco Lofts",
    "Miami Villas",
    "Chicago Townhouses"
]

@app.route('/suggestion', methods=['POST'])
def get_suggestions():
    user_input = request.json.get("query", "").lower()
    filtered_suggestions = [
        suggestion for suggestion in SUGGESTIONS if user_input in suggestion.lower()
    ]
    return jsonify(filtered_suggestions)

if __name__ == '__main__':
    app.run(debug=True)
