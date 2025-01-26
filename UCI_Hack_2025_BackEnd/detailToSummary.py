import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
def initialize_openai(env_path="openAIAPI.env"):
    """
    Initialize OpenAI client using API key from a specified .env file.
    """
    load_dotenv(dotenv_path=Path(env_path))
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class DetailToSummary:
    def __init__(self, client):
        """
        Initialize the DetailToSummary assistant with an OpenAI client.
        """
        self.client = client

    def generate_summary(self, user_input):
        """
        Generate a detailed summary based on user input.

        Parameters:
        - user_input (str): A string containing detailed house features.

        Returns:
        - str: A detailed and appealing summary of the house.
        """
        # Prepare the prompt
        prompt = (
            "You are a creative assistant helping to describe a house. Based on the following details, "
            "write a detailed and appealing summary of the house:\n\n"
        )
        prompt += user_input
        prompt += "\n\nWrite a coherent and descriptive paragraph about the house."

        # Call the OpenAI API
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o-mini"  # Ensure the correct model is specified
        )

        # Extract and return the response
        return chat_completion.choices[0].message.content

# Example usage as an importable module
def detail_to_summary(user_input, env_path="openAIAPI.env"):
    """
    Generate a house summary based on user input.

    Parameters:
    - user_input (str): A string containing house details provided by the user.
    - env_path (str): Path to the .env file containing the OpenAI API key.

    Returns:
    - str: A detailed house summary.
    """
    # Initialize OpenAI client
    client = initialize_openai(env_path)

    # Initialize the assistant
    assistant = DetailToSummary(client)

    # Generate and return the house summary
    return assistant.generate_summary(user_input)

# Main guard for testing purposes
if __name__ == "__main__":
    sample_input = (
        "What is the kitchen like? The kitchen is modern with stainless steel appliances.\n"
        "Describe the living room. The living room is spacious with a fireplace and large windows.\n"
        "What type of flooring does the house have? Hardwood floors throughout.\n"
        "Does the house have any special features? The house has a waterfront view and a large deck.\n"
        "Are there any additional details you'd like to include? A garden with a variety of flowers and fruit trees."
    )
    print(detail_to_summary(sample_input))
