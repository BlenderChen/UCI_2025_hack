from flask import Flask, request, jsonify, Response
from flask_cors import CORS
#HelloWorld
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
    
@app.route('/suggestions123', methods=['GET'])
def get_suggestions():
    # Example suggestions list (can be fetched from a database instead)
    request.args.get('query', '').lower()
    suggestions = results()
    return jsonify(suggestions)

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

