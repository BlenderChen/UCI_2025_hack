from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React front end

def get_address():
    return ["123 Main St", "456 Elm St", "789 Oak St"]

def results():
    return [
    "Rock",
    "Hill",
    "Mountain",
    "Patio",
    "Ocean",
    "Valley",
    "Canyon",
    "Ridge",
    "Peak",
    "Cliff",
    "Slope",
    "Plain",
    "Plateau",
    "Bluff",
    "Crag",
    "River",
    "Stream",
    "Brook",
    "Lagoon",
    "Lake",
    "Pond",
    "Waterfall",
    "Bay",
    "Fjord",
    "Estuary",
    "Grove",
    "Meadow",
    "Glade",
    "Thicket",
    "Woodland",
    "Jungle",
    "Prairie",
    "Savannah",
    "Copse",
    "Dune",
    "Oasis",
    "Wasteland",
    "Mesa",
    "Steppe",
    "Scrubland",
    "Deck",
    "Courtyard",
    "Pergola",
    "Terrace",
    "Veranda",
    "Gazebo",
    "Arbor",
    "Lawn",
    "Garden",
    "Beach",
    "Shore",
    "Coast",
    "Sandbar",
    "Peninsula",
    "Island",
    "Reef",
    "Tidepool",
    "Archipelago",
    "Breeze",
    "Gale",
    "Storm",
    "Cloud",
    "Mist",
    "Fog",
    "Thunder",
    "Lightning",
    "Rain",
    "Snow",
    "Horizon",
    "Sunset",
    "Sunrise",
    "Twilight",
    "Panorama",
    "Landscape",
    "Vista",
    "Outlook",
    "Overlook"
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

def find_dictionary_by_value(json_file, key, value):
    """
    Searches for a dictionary in a JSON file where the specified key matches the given value.
    """
    with open(json_file, "r") as file:
        data = json.load(file)  # Load JSON into Python
        # Search for the dictionary with the matching key-value pair
        for item in data:
            if item.get(key) == value:
                return item
    return None

@app.route('/get_data', methods=['GET'])
def get_data():
    dictionary1 = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
    dictionary2 = {"keyA": "valueA", "keyB": "valueB", "keyC": "valueC", "keyD": "valueD"}
    dictionary3 = {"keyX": "valueX", "keyY": "valueY", "keyZ": "valueZ", "keyZZ": "valueZZ"}

    response = {
        "dictionary1": dictionary1,
        "dictionary2": dictionary2,
        "dictionary3": dictionary3,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)