from flask import Flask, render_template, request, jsonify
from chat import get_response 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.post("/predict")
def predict():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Get a response from the chatbot
    response_message = get_response(user_message)
    
    return jsonify({"answer": response_message})

if __name__ == "__main__":
    app.run(debug=True)
