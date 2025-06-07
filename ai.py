import os
from openai import OpenAI
from dotenv import load_dotenv

# load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❗ Please set your OPENAI_API_KEY in .env")
    exit()

# initialize OpenAI client
client = OpenAI(api_key=api_key)

def call_gpt(prompt, model="gpt-3.5-turbo"):
    system_message = (
        "You are a gentle and empathetic AI counselor who specializes in astrology and emotional intelligence. "
        "You interpret people's emotional states through their zodiac signs, offering comforting, healing, and insightful guidance. "
        "Your tone is warm, supportive, and spiritually uplifting—like that of a life coach or holistic therapist. "
        "Always aim to soothe the user's emotions, help them understand their feelings, and guide them with clarity and compassion."
    )

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❗ GPT Error: {e}")
        return "An error occurred."
