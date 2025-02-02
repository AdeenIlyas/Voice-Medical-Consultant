import os
import base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ELEVEN_LAB_API = os.getenv("ELEVEN_LAB_API")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

prompt = "Analyze observed skin disease in the provided image?"
model = "llama-3.2-90b-vision-preview"

def analyze_image(prompt, model, encoded_image):
    #client = Groq(api_key=GROQ_API_KEY)
    #test
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

#image_encoded = encode_image("acne.jpg")
#print(analyze_image(prompt, model, image_encoded))
