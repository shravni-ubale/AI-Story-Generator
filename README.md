# AI-Story-Generator
# StoryTeller 📚

A magical web application that generates unique stories using AI, crafted with an elegant emerald and gold theme. StoryTeller harnesses the power of Google's Gemini Pro AI to create captivating tales based on your chosen character, setting, and theme.

## Features

- **AI-Powered Storytelling**: Leverage Google's Gemini Pro model for creative story generation
- **Interactive Interface**: Simple and elegant three-parameter story creation
- **Custom Theme**: Beautiful emerald and gold design with smooth animations
- **Responsive Design**: Works seamlessly across different screen sizes
- **Real-time Generation**: Instant story creation with visual feedback

## Getting Started

### Prerequisites

- Python 3.x
- Google API key for Gemini Pro
- Git (for cloning the repository)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/storyteller.git
cd storyteller
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install streamlit google-generativeai python-dotenv
```

4. Create a `.env` file in the project root and add your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

### Running the Application

1. Start the Streamlit server:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Usage

1. Enter a character in the first input field (e.g., "a brave knight")
2. Specify a setting in the second field (e.g., "in a crystal cave")
3. Choose a theme in the third field (e.g., "mystery")
4. Click "Generate Story" to create your tale
5. Wait a moment while the AI weaves your story
6. Read and enjoy your unique creation!

## Customization

The application uses a custom emerald and gold theme. To modify the appearance:

1. Find the CSS section in the code (marked with `st.markdown("""<style>...</style>""")`)
2. Adjust the color variables:
   - Base color: `#013220` (Dark emerald)
   - Text color: `#e2c091` (Gold)
   - Accent color: `#c9a15b` (Light gold)

## Project Structure

```
storyteller/
├── app.py              # Main application file
├── .env                # Environment variables (create this)
├── README.md           # Project documentation
├── UPDATES.md          # Version history and updates
└── requirements.txt    # Project dependencies
```

## Security

- Keep your `.env` file secure and never commit it to version control
- Regularly update your dependencies to patch security vulnerabilities
- Monitor your API usage to stay within Google's limits

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

- Google's Gemini Pro AI model for story generation
- Streamlit for the web application framework
- The open-source community for inspiration and resources

## Support

For support, please:
- Open an issue in the repository
- Contact the maintainer
- Check the Streamlit and Google Gemini documentation

---

Created by Shravni Ubale
