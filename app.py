from flask import Flask, request, Response

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

if __name__ == "__main__":
    app.run(debug=True, port=5001)

