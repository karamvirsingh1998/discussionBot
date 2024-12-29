import os
import openai


def process_request(user_input):
    """
    Process user input and get a response from OpenAI's GPT model.

    Args:
        user_input (str): Input text from the user.

    Returns:
        str: Response text from the model.
    """
    openai.api_key = os.environ.get(
        "OPENAI_API_KEY"
    )  # Use environment variable for API key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}]
    )

    return response["choices"][0]["message"]["content"]
