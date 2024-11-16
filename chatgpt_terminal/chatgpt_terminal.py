import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_gpt(prompt):
    try:
        # Use the correct method to create a chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # System message to define behavior
                {"role": "user", "content": prompt}  # User's input prompt
            ]
        )
        # Return the assistant's reply from the response
        return response['choices'][0]['message']['content']
    except openai.OpenAIError as e:
        # Handle errors from the OpenAI API
        return f"OpenAI API Error: {e}"

if __name__ == "__main__":
    # Print a welcome message and instructions to exit the chat
    print("ChatGPT Terminal. Type 'exit' to end.\n")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break  # Exit the loop if the user types 'exit'
        try:
            # Get the response from the chatbot based on user input
            response = chat_with_gpt(user_input)
            print("ChatGPT:", response)
        except Exception as e:
            # Handle any general errors that occur
            print("An error occurred:", e)




