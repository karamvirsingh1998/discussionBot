# Discussion Bot

This project is a discussion bot built using Streamlit that allows users to interact through voice. The bot transcribes spoken input, processes it using a large language model (LLM), and responds with synthesized speech using OpenAI's TTS API.

## Features

- **Audio Input**: Users can record their voice or upload audio files for transcription.
- **Transcription**: Converts speech to text using Deepgram's API.
- **Processing**: Utilizes OpenAI's GPT model to generate responses.
- **Text-to-Speech**: Converts the bot's text responses into speech using OpenAI's TTS API.

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/discussion-bot.git
cd discussion-bot


2. Install the required packages:
pip install -r requirements.txt


3. Set up your Deepgram and OpenAI credentials as environment variables:
- For OpenAI:
  ```
  export OPENAI_API_KEY='your_openai_api_key'
  ```
- For Deepgram (if not hardcoded in code):
  ```
  export DEEPGRAM_API_KEY='your_deepgram_api_key'
  ```

## Usage

Run the Streamlit application:
streamlit run app.py


Upload an audio file or use the microphone to interact with the bot!

## License

This project is licensed under the MIT License.
Conclusion
With these updates, your discussion-bot project should be fully integrated with Deepgram for transcription functionality. Make sure you have all necessary dependencies installed and that your API keys are correctly set up in your environment variables before running the application. If you encounter any issues or need further assistance, feel free to ask!
