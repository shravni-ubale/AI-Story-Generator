from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Get API key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Route to render the frontend
@app.route('/')
def home():
    return render_template('index.html')

# Route to process the form data and generate a story using Gemini API
@app.route('/process', methods=['POST'])
def process():
    try:
        # Get the form data
        character = request.form['character']
        setting = request.form['setting']
        theme = request.form['theme']

        # Create a prompt for the AI
        prompt = f"Create a story with a {theme} theme featuring {character} in a {setting}."

        # Send the prompt to the Gemini API
        response = chat.send_message(prompt)

        # Return the generated story as JSON
        result = {
            "character": character,
            "setting": setting,
            "theme": theme,
            "story": response.text
        }
        return jsonify(result)

    except Exception as e:
        # Handle any errors
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
