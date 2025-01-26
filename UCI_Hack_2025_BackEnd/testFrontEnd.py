from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React front end

# Function to provide mock results
def get_results():
    return [
        "New York Apartments",
        "Los Angeles Condos",
        "San Francisco Lofts",
        "Miami Villas",
        "Chicago Townhouses"
    ]

# Root route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route to handle search queries
@app.route('/api/search', methods=['POST'])
def search():
    data = request.json  # Get JSON data from the request
    query = data.get('query', '')  # Extract the 'query' parameter
    print(f"User Input: {query}")

    # Simulate a search process (replace this with your logic, e.g., database query)
    results = get_results()
    filtered_results = [item for item in results if query.lower() in item.lower()]

    return jsonify({"results": filtered_results})

# Route to provide suggestions
@app.route('/getsuggestions', methods=['GET'])
def get_suggestions():
    query = request.args.get('query', '').lower()  # Get query parameter
    suggestions = get_results()

    # Optionally filter suggestions based on the query
    if query:
        suggestions = [item for item in suggestions if query in item.lower()]

    return jsonify(suggestions)

# Route to handle raw query processing
@app.route('/suggestions', methods=['GET'])
def get_query():
    query = request.args.get('query', '')  # Retrieve query parameter
    print(f"Received query: {query}")

    if not query:
        return jsonify({"message": "Query parameter is missing"}), 400

    # Return the processed query
    return jsonify({"query": query + " this is python operating on the data"})

if __name__ == '__main__':
    app.run(debug=True)
