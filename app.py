import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables and configure API
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def generate_story(character, setting, theme):
    """Generate a story using the Gemini API"""
    try:
        prompt = f"Create a story with a {theme} theme featuring {character} in a {setting}."
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error generating story: {str(e)}"


# Set page configuration
st.set_page_config(
    page_title="StoryTeller",
    page_icon="📚",
    layout="centered"
)

# Custom CSS for Times New Roman and professional theme
st.markdown("""
    <style>
    .stApp {
        background-color: #f9f9f9;
    }
    h1, h2, h3, h4, h5, h6, .stMarkdown, .stTextInput>div>div, footer {
        font-family: 'Times New Roman', serif;
        color: #2c1810;
    }
    h1 {
        color: #8b4513;
    }
    .stTextInput>div>div {
        background-color: #ffffff;
        border: 2px solid #dcdcdc;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #8b4513;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.8em 1.5em;
    }
    .stButton>button:hover {
        background-color: #703810;
    }
    .stAlert, .stMarkdown pre {
        background-color: #ffffff;
        border: 2px solid #dcdcdc;
        border-radius: 8px;
        padding: 1em;
        color: #2c1810;
    }
    footer {
        text-align: center;
        margin-top: 2em;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True)

# Add a title and description
st.title("StoryTeller")
st.markdown("""
    Whisper your tale, and let the magic unfold!
""")

# Inputs for character, setting, and theme
col1, col2, col3 = st.columns(3)

with col1:
    character = st.text_input(
        "Character",
        placeholder="e.g., a daring explorer"
    )

with col2:
    setting = st.text_input(
        "Setting",
        placeholder="e.g., in an enchanted forest"
    )

with col3:
    theme = st.text_input(
        "Theme",
        placeholder="e.g., adventure"
    )

# Generate the story
if st.button("Generate Story"):
    if character and setting and theme:
        with st.spinner("Weaving your tale..."):
            story = generate_story(character, setting, theme)
            st.success("Here's your story:")
            st.markdown(f"""
                <div style="padding: 15px; background-color: #ffffff; border: 1px solid #dcdcdc; border-radius: 8px;">
                <p style="font-family: 'Times New Roman', serif; color: #2c1810;">{story}</p>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"**Character**: {character}  \n**Setting**: {setting}  \n**Theme**: {theme}")
    else:
        st.error("Please fill in all fields before generating a story.")

# Footer
st.markdown("---")
st.markdown("<footer>Woven with care by the Story Weaver.</footer>", unsafe_allow_html=True)
