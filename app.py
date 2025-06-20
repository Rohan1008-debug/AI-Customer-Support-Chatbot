from flask import Flask, request, jsonify, render_template
import random
import json

app = Flask(__name__)

# Load intents
with open('intents.json') as f:
    intents = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_msg = request.form["msg"]
    for intent in intents["intents"]:
        if user_msg.lower() in [p.lower() for p in intent["patterns"]]:
            return random.choice(intent["responses"])
    return "I'm sorry, I didn't understand that."

if __name__ == "__main__":
    app.run(debug=True)
