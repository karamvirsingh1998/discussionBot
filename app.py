import streamlit as st
import asyncio
import io
import os
from streamlit_mic_recorder import mic_recorder
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

# Initialize Deepgram Client
DEEPGRAM_API_KEY = os.environ.get(
    "DEEPGRAM_API_KEY"
)  # Ensure this is set in your environment variables
deepgram = DeepgramClient(DEEPGRAM_API_KEY)


async def transcribe_audio(audio_bytes):
    payload: FileSource = {
        "buffer": audio_bytes,
    }
    source = {"buffer": audio_bytes, "mimetype": "audio/wav"}

    try:
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)
        print(response)
        if response and "channel" in response:
            alternatives = response["channel"]["alternatives"]
            if alternatives:
                return alternatives[0]["transcript"]
            else:
                print("No alternatives found in the response.")
                return None
        else:
            print("Invalid response structure:", response)
            return None
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


def main():
    st.title("Discussion Bot")

    if "history" not in st.session_state:
        st.session_state.history = []

    st.subheader("Speak to the Bot:")

    # Record audio (assuming mic_recorder is correctly implemented)
    audio = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording")

    if audio and "bytes" in audio:
        print(f"Audio bytes size: {len(audio['bytes'])}")  # Check size of audio bytes

        # Process the recorded audio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        transcribed_text = loop.run_until_complete(transcribe_audio(audio["bytes"]))

        if transcribed_text:
            st.session_state.history.append(f"You: {transcribed_text}")
            response = process_request(transcribed_text)
            st.session_state.history.append(f"Bot: {response}")
            audio_path = synthesize_speech(response)
            st.audio(audio_path)
    else:
        st.error("No audio was recorded.")

    # Option to upload an audio file
    audio_file = st.file_uploader("Or upload Audio", type=["wav", "mp3"])

    if audio_file is not None:
        # Read the uploaded audio file into bytes
        audio_bytes = io.BytesIO(audio_file.read()).getvalue()

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        transcribed_text = loop.run_until_complete(transcribe_audio(audio_bytes))

        if transcribed_text:
            st.session_state.history.append(f"You: {transcribed_text}")
            response = process_request(transcribed_text)
            st.session_state.history.append(f"Bot: {response}")
            audio_path = synthesize_speech(response)
            st.audio(audio_path)

    st.subheader("Conversation History:")
    for message in st.session_state.history:
        st.write(message)


if __name__ == "__main__":
    main()
