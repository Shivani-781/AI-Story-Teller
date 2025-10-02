# AI Story Teller

AI Story Teller is a Streamlit web app that generates creative stories and narrations based on user-uploaded images and selected genres. Powered by Google Gemini, it connects your images into a single narrative and provides audio narration.

## Features

- Upload up to 10 images as story inspiration
- Choose from multiple story styles (Fairy Tale, Adventure, Sci-Fi, Mystery, Romance, Horror, Comedy, Drama, Morale)
- AI generates a story connecting all images
- Listen to the story narration in English

## Getting Started

### Prerequisites

- Python 3.8+
- [Google API Key](https://ai.google.dev/)
- The following Python packages (see [requirements.txt](requirements.txt)):
  - streamlit
  - python-dotenv
  - google-genai
  - Pillow
  - gTTS
  - dotenv

### Installation

1. Clone this repository.
2. Add your Google API key to a `.env` file
3. Install dependencies: `pip install -r requirements.txt`

### Running the App
`streamlit run app.py`

## Usage
1. Open the app in your browser.
2. Upload up to 10 images.
3. Select your preferred story style.
4. Click "Generate Story & Narration" to view and listen to your AI-generated story.

## Demo
Access the app here: https://genai-story-teller.streamlit.app/
