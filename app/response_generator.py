# app/response_generator.py

"""
ResponseGenerator:
- Takes:
    - user_message (str)
    - memory (dict from MemoryExtractor)
- Produces:
    - "before": neutral response
    - "after": personality-aware response
    - "persona_mode": which persona was applied
"""

from typing import Dict, Any, List


class ResponseGenerator:
    def __init__(self) -> None:
        pass

    # -------- Persona selection logic --------
    def _infer_persona(self, memory: Dict[str, Any]) -> str:
        """
        Very simple logic:
        - If any emotional pattern is negative → therapist_style
        - Else if any preference sounds fun/travel/positive → witty_friend
        - Else → calm_mentor
        """
        emos: List[Dict[str, Any]] = memory.get("emotional_patterns") or []
        prefs: List[Dict[str, Any]] = memory.get("preferences") or []

        if any(e.get("emotion") == "negative" for e in emos):
            return "therapist_style"

        if any(
            any(word in (p.get("value", "").lower())
                for word in ["travel", "trip", "movie", "music", "food", "fun"])
            for p in prefs
        ):
            return "witty_friend"

        return "calm_mentor"

    # -------- Base "before" response --------
    def _neutral(self, user_message: str) -> str:
        return (
            f"I understand. You said: {user_message!r}.\n"
            "Here's a straightforward way to look at it."
        )

    # -------- Persona: Calm Mentor --------
    def _as_calm_mentor(self, user_message: str) -> str:
        return (
            "I hear your concern.\n\n"
            f"You're saying: {user_message!r}.\n\n"
            "Let's break this into two parts:\n"
            "1. What exactly is bothering you.\n"
            "2. What is realistically in your control.\n\n"
            "If you're open to it, we can go step-by-step and design one small, practical action "
            "you can try next time this happens."
        )

    # -------- Persona: Witty Friend --------
    def _as_witty_friend(self, user_message: str) -> str:
        return (
            f"Okay, that line — {user_message!r} — is *way* too relatable 😅\n\n"
            "Life would be so much easier if people just replied on time, right?\n"
            "But until that version of the world ships, we can:\n"
            "• Protect your time and energy\n"
            "• Set clearer expectations with people\n"
            "• And not let slow replies ruin your whole mood 💆‍♂️\n\n"
            "Tell me this: do late replies make you more angry, anxious, or just tired of people?"
        )

    # -------- Persona: Therapist Style --------
    def _as_therapist(self, user_message: str) -> str:
        return (
            f"It sounds like this really bothers you: {user_message!r}.\n\n"
            "Your reaction makes sense — feeling ignored or disrespected can be painful.\n"
            "Instead of judging yourself for it, let's look at it with curiosity:\n"
            "• When this happens, what story do you tell yourself?\n"
            "• Does it remind you of how others have treated you before?\n\n"
            "We can unpack this at your pace. There's no rush."
        )

    # -------- Public API --------
    def generate(self, user_message: str, memory: Dict[str, Any]) -> Dict[str, str]:
        before = self._neutral(user_message)
        persona = self._infer_persona(memory)

        if persona == "witty_friend":
            after = self._as_witty_friend(user_message)
        elif persona == "therapist_style":
            after = self._as_therapist(user_message)
        else:
            persona = "calm_mentor"
            after = self._as_calm_mentor(user_message)

        return {
            "before": before,
            "after": after,
            "persona_mode": persona,
        }
