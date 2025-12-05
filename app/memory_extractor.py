import re
from typing import List, Dict


class MemoryExtractor:
    """
    Extracts preferences, emotional patterns, and factual memories
    from a list of user chat messages.
    """

    def extract(self, messages: List[str]) -> Dict:
        preferences = []
        emotions = []
        facts = []

        for msg in messages:
            text = msg.lower()

            # Preferences
            if "i like" in text or "i love" in text:
                preference = text.split("i")[1].strip()
                preferences.append(preference)

            if "i hate" in text or "i don't like" in text:
                preference = text.split("i")[1].strip()
                preferences.append(preference)

            # Emotional patterns
            if any(word in text for word in ["sad", "upset", "tired", "angry", "depressed"]):
                emotions.append({"emotion": "negative", "message": msg})
            if any(word in text for word in ["happy", "excited", "grateful", "amazing", "great"]):
                emotions.append({"emotion": "positive", "message": msg})

            # Facts worth remembering
            if "my name is" in text:
                name = text.split("my name is")[1].strip().title()
                facts.append({"name": name})
            if "i live in" in text:
                location = text.split("i live in")[1].strip().title()
                facts.append({"location": location})

        return {
            "preferences": preferences,
            "emotional_patterns": emotions,
            "facts": facts
        }
