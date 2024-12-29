import os
import openai


def synthesize_speech(text):
    """
    Convert text to speech using OpenAI's TTS API.

    Args:
        text (str): The input text to synthesize.

    Returns:
        str: The path to the generated audio file.
    """

    # Generate speech using OpenAI's TTS API (adjust parameters as needed)
    response = openai.Audio.create(
        model="text-to-speech-1",  # Use appropriate model name for TTS if available; adjust as necessary.
        input=text,
        voice="en-US-Standard",  # Choose a voice from available options.
    )

    # Save the audio response to a file (assuming it returns binary data)
    audio_file_path = "output.wav"

    with open(audio_file_path, "wb") as f:
        f.write(response["audio"])  # Adjust based on actual response structure

    return audio_file_path
