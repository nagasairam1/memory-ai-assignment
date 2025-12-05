from app.personality_engine import PersonalityEngine


class ResponseGenerator:
    """
    Creates before/after AI responses based on personality injection.
    """

    def __init__(self):
        self.personality_engine = PersonalityEngine()

    def generate(self, user_message: str, memory: dict) -> dict:
        base_reply = f"I understand. You said: '{user_message}'. Here's how you can approach it."

        personality = self.personality_engine.choose_personality(memory)
        improved_reply = self.personality_engine.apply_personality(base_reply, personality)

        return {
            "before": base_reply,
            "after": improved_reply,
            "persona_mode": personality
        }
