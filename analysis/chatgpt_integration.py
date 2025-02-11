import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Get the variable
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def format_message(role, content):
    return {"role": role, "content": content}


def get_response(messages):
    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
    )
    content = completion.choices[0].message.content
    return content

posts = [
    "Fossil Fuels destroy the environment",
    "CO2 emissions are rising",
    "More wind turbines need to be constructed"
]

class_inst = 'Identify wheather the posts are fossil fuel, CO2 or renewable energy related'
responses = []
counter = 0
for post in posts:
    counter += 1
    messages = [format_message("system", class_inst),
                format_message("user",post)]
    response = get_response(messages)
    responses.append(f'Post {counter} is {response}')

print(responses)