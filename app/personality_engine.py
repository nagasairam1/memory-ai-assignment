class PersonalityEngine:
    """
    Determines tone of response based on stored memory and user emotional patterns.
    """

    def choose_personality(self, memory: dict) -> str:
        emotions = memory.get("emotional_patterns", [])

        if any(e["emotion"] == "negative" for e in emotions):
            return "therapist"
        if any("joke" in p for p in memory.get("preferences", [])):
            return "witty_friend"
        return "calm_mentor"

    def apply_personality(self, text: str, personality: str) -> str:
        if personality == "therapist":
            return f"I hear you. It sounds difficult. Let's take it slowly — {text}"
        if personality == "witty_friend":
            return f"😂 Okay buddy, real talk — {text}. But hey, you're doing great!"
        return f"Here’s my guidance: {text}"
