from flask import Flask, request, Response, jsonify
from openai import OpenAI
import logging
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Instantiate OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    user_message = data["message"]
    logging.info(f"Received message: {user_message}")

    try:
        # Make the API call to OpenAI using the correct endpoint for the chat model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Chat model
            messages=[{"role": "user", "content": user_message}]
        )
        # Process the response
        message_content = response.choices[0].message.content.strip() if response.choices else "Unable to get a valid response."
        logging.info(f"Received response content: {message_content}")
        return Response(message_content, mimetype="text/plain")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return Response(f"An error occurred while generating the response: {e}", mimetype="text/plain")

@app.route("/chat_with_assistant", methods=["POST"])
def chat_with_assistant():
    # Implement your logic for using OpenAI's assistants feature
    # Placeholder for assistant logic
    pass

@app.route("/retrieve_vectors", methods=["POST"])
def retrieve_vectors():
    # Implement your logic for using OpenAI's vectors feature
    # Placeholder for vectors logic
    pass

@app.route("/tekmetrics_query", methods=["POST"])
def query_tekmetrics():
    # Implement your logic for interacting with the Tekmetrics API
    # Placeholder for Tekmetrics API logic
    pass

# You can add more routes as needed

if __name__ == "__main__":
    app.run(debug=True, port=5001)
