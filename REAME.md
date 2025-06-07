# 🌟 Starlight Angel Healing

**Starlight Angel Healing** is an AI-powered emotional support tool that provides healing advice based on your zodiac sign and emotional state. It uses OpenAI's GPT models to generate comforting, poetic, and insightful messages to guide users through emotional moments.

🪐 Built with Python, this tool is designed for personal reflection, daily emotional check-ins, or just a gentle reminder that you're doing your best.

---

## ✨ Features

- Personalized advice based on zodiac, mood, and situation
- Customizable tone (e.g., calm, poetic)
- Modular design for easy expansion (CLI now, GUI later)
- Powered by OpenAI GPT-3.5 Turbo API

---

## 🚀 How to Run Locally


### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up your OpenAI API key

1. Copy the example .env file:

```bash
   cp .env.example .env
```

2. Go to OpenAI and generate your API key:
   👉 https://platform.openai.com/account/api-keys

3. Open your .env file and paste the key like this:

```bash
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

4. If you haven't already, make sure to add a payment method in your OpenAI account to activate your API usage.

### 3. Run the program

```bash
python main.py
```

The tool will use either test data or your input to generate a personalized healing message ✨
