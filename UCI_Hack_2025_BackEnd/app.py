from flask import Flask, jsonify, request
from flask_cors import CORS
import json
#UCI_Hack_2025_BackEnd/fsrc

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

if __name__ == '__main__':
    # app.run(debug=True)
    # file = open("UCI_Hack_2025_BackEnd/fsrc/house.txt", 'r')
    json_file = "UCI_Hack_2025_BackEnd/fsrc/properties.json"
    key_to_search = "price"
    value_to_search = 430145

    result = find_dictionary_by_value(json_file, key_to_search, value_to_search)

    if result:
        print("Found dictionary:", result)
    else:
        print(f"No dictionary found with {key_to_search} = {value_to_search}")


def find_dictionary_by_value(json_file, key, value): 
    with open(json_file, "r") as file:
        data = json.load(file)  # Load JSON into Python
        # Search for the dictionary with the matching key-value pair
        for item in data:
            if item.get(key) == value:
                return item
    return None


    # f = file.readlines()

    # print("hey")
    # print(f)
    # print("hello")





    # Example usage
    # result = find_dict_by_key_value(dat, "name", "Alice")
    # print(result)


    



