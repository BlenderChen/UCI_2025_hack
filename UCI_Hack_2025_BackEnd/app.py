from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React front end

def results():
    return [
        "New York Apartments",
        "Los Angeles Condos",
        "San Francisco Lofts",
        "Miami Villas",
        "Chicago Townhouses"
    ]

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json  # Get JSON data from the request
    query = data.get('query', '')  # Extract the 'query' parameter
    print(f"User Input: {query}")

    # Simulate a search process (replace this with your logic, e.g., database query)
    suggestions = results()
    filtered_results = [item for item in suggestions if query.lower() in item.lower()]

    return jsonify({"results": filtered_results})
    
@app.route('/getsuggestions', methods=['GET'])
def get_suggestions():
    # Retrieve the 'query' parameter from the request arguments
    user_input = request.args.get("query", "").lower()

    # Example suggestions list (can be fetched from a database instead)
    suggestions = results()

    # Filter suggestions based on the user input
    filtered_suggestions = [
        suggestion for suggestion in suggestions if user_input in suggestion.lower()
    ]
    return jsonify(filtered_suggestions)

@app.route('/suggestions', methods=['GET'])
def get_query():
    print("hello")
    # Retrieve the raw query parameter from the request
    query = request.args.get('query', '')

    # Log the received query for debugging purposes
    print(f"Received query: {query}")

    # Return the query as-is in the response
    return jsonify({"query": query + " this is python operating on the data"})

if __name__ == '__main__':
    app.run(debug=True)
