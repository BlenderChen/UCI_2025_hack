from flask import Flask, request, jsonify
from flask_cors import CORS
from textToAddress import textToAddress
from detailToSummary import detail_to_summary

textToAddress = textToAddress(dataset_path='Houses.csv')
k=3

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your React front end

dictionary1 = {"Address": "value1", "Price": "value2", "Link": "value3", "Year": "value4", "Summary": "key1"}
dictionary2 = {"Address": "valueA", "Price": "valueB", "Link": "valueC", "Year": "valueD", "Summary": "key2"}
dictionary3 = {"Address": "valueX", "Price": "valueY", "Link": "valueZ", "Year": "valueZ", "Summary": "key3"}
def get_address(input):
    # Find the nearest houses using textToAddress
    top_houses = textToAddress.find_nearest_houses(input, k)
    
    # Use global dictionaries
    global dictionary1, dictionary2, dictionary3

    def convert_to_serializable(dictionary, house):
        """
        Converts a dictionary's values to JSON-serializable types.
        """
        dictionary["Address"] = str(house["Address"])  # Ensure it's a string
        dictionary["Price"] = float(house["Price"])    # Convert to float
        dictionary["Link"] = str(house["Link"])        # Ensure it's a string
        dictionary["Year"] = int(house["Year"])        # Convert to int
        dictionary["Summary"] = str(detail_to_summary(house.get("Details", ""))) # Ensure it's a string

    # Update dictionaries with serializable types
    if len(top_houses) >= 1:
        convert_to_serializable(dictionary1, top_houses[0])
    if len(top_houses) >= 2:
        convert_to_serializable(dictionary2, top_houses[1])
    if len(top_houses) >= 3:
        convert_to_serializable(dictionary3, top_houses[2])

    # Convert data to JSON-serializable format
    return [
        {
            "Details": str(house["Details"])  # Ensure it's a string
        }
        for house in top_houses
    ]



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



# @app.route('/suggestions', methods=['GET'])
# def get_query():
    
#     query = request.args.get('query', '')

#     # Log the received query for debugging purposes
#     print(f"Received query: {query}")

#     # Update placeholderArray
#     query = get_address(query)

#     # Return a response with the updated placeholderArray
#     return jsonify({"query": query})
@app.route('/suggestions', methods=['GET'])
def get_query():
    user_input = request.args.get('query', '')

    print(f"Received query: {user_input}")

    addresses = get_address(user_input)

    # Return as "results" or "addresses" instead of "query"
    return jsonify({"results": addresses})




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

    response = {
        "dictionary1": dictionary1,
        "dictionary2": dictionary2,
        "dictionary3": dictionary3,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)