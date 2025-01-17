import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


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


st.set_page_config(
    page_title="StoryTeller",
    page_icon="📚",
    layout="centered"
)


st.markdown("""
    <style>
    .stApp {
        background-color: #013220; /* Dark emerald green base */
        background-image: linear-gradient(to bottom right, rgba(1, 50, 32, 0.9), rgba(24, 45, 40, 0.9)), 
                          url('https://www.transparenttextures.com/patterns/dark-matter.png'); 
        color: #e2c091 !important; 
    }
    h1, h2, h3, h4, h5, h6, .stMarkdown, footer {
        font-family: 'Times New Roman', serif;
        color: #e2c091 !important;
    }
    h1 {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .stTextInput>div>div {
        background-color: rgba(40, 80, 60, 0.9); 
        border: 2px solid #e2c091;
        border-radius: 8px;
        color: #e2c091 !important;
    }
    .stTextInput>div>div input {
        color: #e2c091 !important;
    }
    .stTextInput>div>div:focus-within {
        border-color: #c9a15b;
    }
    label {
        color: #e2c091 !important;
    }
    .stButton>button {
        background-color: #013220;
        color: #e2c091 !important;
        border: 2px solid #e2c091;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.8em 1.5em;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #024d30;
        border-color: #c9a15b;
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(201, 161, 91, 0.3);
    }
    .stAlert, .stMarkdown pre {
        background-color: #013220;
        border: 2px solid #e2c091;
        border-radius: 8px;
        color: #e2c091 !important;
    }
    footer {
        text-align: center;
        margin-top: 2em;
        font-size: 0.9em;
        color: #e2c091 !important; 
    }
    input::placeholder {
        color: #e2c091 !important;
    }
    </style>
    """, unsafe_allow_html=True)


st.title("StoryTeller")
st.markdown("""
    Spin the emerald threads of imagination, and let a golden tale emerge!
""")


col1, col2, col3 = st.columns(3)

with col1:
    character = st.text_input(
        "Character",
        placeholder="e.g., a daring explorer",
        key="character"
    )

with col2:
    setting = st.text_input(
        "Setting",
        placeholder="e.g., in an enchanted forest",
        key="setting"
    )

with col3:
    theme = st.text_input(
        "Theme",
        placeholder="e.g., adventure",
        key="theme"
    )


if st.button("Generate Story"):
    if character and setting and theme:
        with st.spinner("Weaving your golden tale..."):
            story = generate_story(character, setting, theme)
            st.success("Here's your story:")
            st.markdown(f"""
                <div style="padding: 15px; background-color: #013220; border: 1px solid #e2c091; border-radius: 8px;">
                <p style="font-family: 'Times New Roman', serif; color: #e2c091;">{story}</p>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"**Character**: {character}  \n**Setting**: {setting}  \n**Theme**: {theme}")
    else:
        st.error("Please fill in all fields before generating a story.")


st.markdown("---")
st.markdown("<footer>Created with care by the Story Weaver.</footer>", unsafe_allow_html=True)
