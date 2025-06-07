from ai import call_gpt
from prompts import build_prompt

def main():
    print("🪐 Zodiac Mood Advice Tool")

    user_data = {
        "zodiac": input("What is your zodiac sign?: "),
        "mood": input("How are you feeling right now?: "),
        "today": input("What happened today? (optional): "),
        "description": input("Anything else you'd like to share? (optional): "),
        "healing_style": input("What kind of tone do you prefer? (optional): ")
    }


    prompt = build_prompt(user_data)
    response = call_gpt(prompt)
    
    print("\n✨ Here's some advice for you:")
    print(response)

if __name__ == "__main__":
    main()
