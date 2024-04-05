import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_KEY"])


def generate_story(input_text):
    # Call the OpenAI API to generate the story
    response = get_story(input_text)
    # Format and return the response
    return format_response(response)


def get_story(input_text):
    # Construct the system prompt. Feel free to experiment with different prompts.
    system_prompt = f"""You are a story generator.
    You will be provided with a description about the story the user wants.
    Write a story using the description provided."""
    # Make the API call
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text},
        ],
        temperature=0.8,
    )

    # Return the API response
    return response


def format_response(response):
    # Extract the generated story from the response
    story = response.choices[0].message.content
    # Remove any unwanted text or formatting
    story = story.strip()
    # Return the formatted story
    return story


# For testing purposes
if __name__ == "__main__":
    user_input = "Tell me a story about a dragon"
    print(generate_story(user_input))
