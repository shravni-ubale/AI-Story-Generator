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
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY is not set in the environment variables.")

# Configure Gemini API
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
except Exception as api_error:
    raise RuntimeError(f"Failed to configure Gemini API: {api_error}")

# Route to render the frontend
@app.route('/')
def home():
    return render_template('index.html')

# Route to process the form data and generate a story using Gemini API
@app.route('/process', methods=['POST'])
def process():
    try:
        # Validate form inputs
        character = request.form.get('character')
        setting = request.form.get('setting')
        theme = request.form.get('theme')

        if not character or not setting or not theme:
            raise ValueError("All fields (character, setting, and theme) must be provided.")

        # Create a prompt for the AI
        prompt = f"Create a story with a {theme} theme featuring {character} in a {setting}."

        # Send the prompt to the Gemini API
        response = chat.send_message(prompt)
        if not response or not response.text:
            raise RuntimeError("The AI response was empty or invalid.")

        # Return the generated story as JSON
        result = {
            "character": character,
            "setting": setting,
            "theme": theme,
            "story": response.text
        }
        return jsonify(result)

    except ValueError as ve:
        return jsonify({"error": f"Validation Error: {str(ve)}"}), 400
    except RuntimeError as re:
        return jsonify({"error": f"Runtime Error: {str(re)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected Error: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
