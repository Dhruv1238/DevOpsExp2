from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # Get JSON data from the POST request
    data = request.get_json()
    
    # Print the received data to the CLI
    print("Received data:", data)
    
    # Respond with a confirmation message
    return jsonify({"message": "Data received successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
