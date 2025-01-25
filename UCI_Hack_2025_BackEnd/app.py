from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React front end

def results():
    return ["New York Apartments",
        "Los Angeles Condos",
        "San Francisco Lofts",
        "Miami Villas",
        "Chicago Townhouses"]

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json  # Get JSON data from the request
    query = data.get('query', '')  # Extract the 'query' parameter
    print(f"User Input: {query}")

    # Simulate a search process (replace this with your logic, e.g., database query)
    results = results()
    filtered_results = [item for item in results if query.lower() in item.lower()]

    return jsonify({"results": filtered_results})
    
@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    # Example suggestions list (can be fetched from a database instead)
    suggestions = results()
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(debug=True)

