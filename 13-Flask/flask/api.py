### Put and Delete -HTTP Verbs
### Working with APIs --Jsonify
### Working with APIs --Request Object

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

##Initial Data in my to do list

items = [
    {"id": 1, "name": "Item 1", "description": "this is item 1"},
    {"id": 2, "name": "Item 2", "description": "this is item 2"},
    {"id": 3, "name": "Item 3", "description": "this is item 3"}
]

@app.route("/")
def home():
    return "Welcome to the Sample to do list"

## Get: retrives all the items in the list
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

## get: retrive a specific item based on the id
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404
    
## Post: create a new task - API
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify({"message": "Request body must be JSON"}), 400
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)

# put: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])

    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
