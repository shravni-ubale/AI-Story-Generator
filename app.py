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
    page_title="AI Story Generator",
    page_icon="📚",
    layout="centered"
)

# Add a title and description
st.title("🤖 AI Story Generator")
st.markdown("""
    Welcome to the AI Story Generator! Enter your story preferences below,
    and let AI create a unique story just for you.
""")

# Create three columns for inputs
col1, col2, col3 = st.columns(3)

with col1:
    character = st.text_input(
        "Main Character",
        placeholder="e.g., a brave astronaut"
    )

with col2:
    setting = st.text_input(
        "Setting",
        placeholder="e.g., on Mars"
    )

with col3:
    theme = st.text_input(
        "Theme",
        placeholder="e.g., adventure"
    )

# Add a generate button
if st.button("Generate Story", type="primary"):
    if character and setting and theme:
        with st.spinner("Generating your story..."):
            story = generate_story(character, setting, theme)

            # Display the story in a nice format
            st.success("Story generated successfully!")
            st.markdown("### Your Story")
            st.markdown(story)

            # Add details about the story parameters
            st.markdown("### Story Details")
            st.markdown(f"""
            - **Character**: {character}
            - **Setting**: {setting}
            - **Theme**: {theme}
            """)
    else:
        st.error("Please fill in all fields before generating a story.")

# Add a footer
st.markdown("---")
st.markdown(
    "Made with ❤️ using Streamlit and Google's Gemini AI"
)