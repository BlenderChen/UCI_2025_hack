from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React front end

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json  # Get JSON data from the request
    query = data.get('query', '')  # Extract the 'query' parameter
    print(f"User Input: {query}")

    # Simulate a search process (replace this with your logic, e.g., database query)
    results = [
        "New York Apartments",
        "Los Angeles Condos",
        "San Francisco Lofts",
        "Miami Villas",
        "Chicago Townhouses"
    ]
    filtered_results = [item for item in results if query.lower() in item.lower()]

    return jsonify({"results": filtered_results})

if __name__ == '__main__':
    app.run(debug=True)
