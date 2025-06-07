def build_prompt(data):
    """
    Converts user input into a natural language prompt for the AI.
    `data` is a dictionary with optional keys:
    - zodiac
    - mood
    - today
    - description
    - healing_style
    """
    # Header: instructions for the AI
    parts = [
        "You are a compassionate AI astrology counselor who specializes in emotional healing.",
        "Based on the following information, please provide a 100–150 word piece of supportive advice:",
    ]

    # Basic information
    zodiac = data.get('zodiac', 'Unknown')
    mood = data.get('mood', '')

    parts.append(f"- Zodiac sign: {zodiac}")
    parts.append(f"- Current mood: {mood}")

    # Optional fields (optional)
    optional_fields = {
        "today": "Situation today",
        "description": "Additional context",
        "healing_style": "Preferred tone/style of the response"
    }

    for key, label in optional_fields.items():
        value = data.get(key)
        if value:
            parts.append(f"- {label}: {value}")

    # supplementary instructions
    parts.append(
        "Please use a gentle, empathetic tone and incorporate the personality traits commonly associated with the user's zodiac sign in your healing message."
    )

    return "\n".join(parts)
