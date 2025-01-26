import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Specify the custom .env file path
env_path = Path("openAIAPI.env")  # Replace with the actual path
load_dotenv(dotenv_path=env_path)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_user():
    print("Hello! I'm your house description assistant powered by ChatGPT. 😊")
    print("Let's create a detailed description of your house. I'll ask you a few questions.")

    # Gather user inputs
    user_inputs = []
    questions = [
        "What is the kitchen like? (e.g., modern, spacious, rustic)",
        "Describe the living room. (e.g., cozy, with a fireplace, open floor plan)",
        "What type of flooring does the house have? (e.g., hardwood floors, tile, carpet)",
        "Does the house have any special features? (e.g., waterfront, two-story, modern design)",
        "Are there any additional details you'd like to include? (e.g., garden, swimming pool, location)"
    ]

    for question in questions:
        response = input(f"{question}\n> ")
        user_inputs.append(f"{question} {response}")

    # Prepare the prompt
    prompt = (
        "You are a creative assistant helping to describe a house. Based on the following details, "
        "write a detailed and appealing description of the house:\n\n"
    )
    prompt += "\n".join(user_inputs)
    prompt += "\n\nWrite a coherent and descriptive paragraph about the house."

    # Call the OpenAI API using the new syntax
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o-mini",  # Ensure the correct model is specified
    )

    # Extract and display the response
    house_description = chat_completion.choices[0].message.content  # Use dot notation
    print("\nHere is the detailed description of your house:")
    print(house_description)

# Run the chatbot
if __name__ == "__main__":
    chat_with_user()
