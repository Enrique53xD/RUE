import os
from flask import Flask, jsonify

app = Flask(__name__)

# This is your main API endpoint
@app.route("/api/v1/hello")
def get_hello():
  # Return some simple JSON
  return jsonify(
    message="Hello from your Railway API!",
    status="success"
  )

# A route to test your API is alive
@app.route("/")
def get_home():
  return "The API server is running."

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))