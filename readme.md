 GupShupp Assignment — Companion AI (Memory + Personality Engine)

This project demonstrates:

- 🧠 **Memory extraction** from a batch of ~30 user chat messages  
- 🎭 **Personality-based response engine** (calm mentor / witty friend / therapist-style)  
- 🔁 **Before/After tone transformation** for the same reply  

Everything runs **fully locally** using Python + Streamlit.  
No external APIs or keys are required.

---

 🔧 How to Run (Local)

 1. Create & activate virtual environment (Windows PowerShell)

```bash
cd memory-ai-assignment-main

python -m venv venv
venv\Scripts\activate
If python is not recognized, install Python from python.org and restart your terminal.

2. Install dependencies
bash

pip install -r requirements.txt
3. Run the Streamlit app
bash

streamlit run main.py
Then open the URL shown in the terminal (usually http://localhost:8501).

💻 How to Use the App
Prepare a JSON file: an array of user messages (strings), ideally 30 messages.

Example structure:

json

[
  "I love travelling and long drives",
  "Sometimes I feel really low when work becomes stressful",
  "My name is Raghav",
  "I prefer short and direct answers"
]
In the UI:

Click “Upload chat messages JSON file (array of 30 messages)”

Select your JSON file (e.g., sample_data/chat_messages.json)

The app will show:

🧩 Extracted Memory

preferences

emotional_patterns

facts

In “Test Personality Response Engine”:

Type a user message (e.g., I hate when people reply very late.)

The app will show:

🔹 Before (Neutral Response)

🔹 After (Personality-Aware Response)

persona_mode (e.g., calm_mentor, witty_friend, therapist_style)

📂 Project Structure
text

memory-ai-assignment-main/
│
├─ app/
│   ├─ memory_extractor.py       Extracts preferences, emotions, facts from messages
│   ├─ response_generator.py     Neutral + personality-aware responses
│   ├─ utils.py                  Helpers (e.g., load_messages)
│
├─ sample_data/
│   └─ chat_messages.json        Example 30-message file for quick demo
│
├─ tests/
│   └─ test_memory_extractor.py  Very simple sanity test
│
├─ main.py                       Streamlit UI entrypoint
├─ requirements.txt
├─ README.md
└─ LICENSE
🧪 Sample Data
Create the folder sample_data (if not already present), then add:

sample_data/chat_messages.json:

json

[
  "I love travelling and long drives",
  "Sometimes I feel really low when work becomes stressful",
  "My name is Raghav",
  "I prefer short and direct answers",
  "Weekends make me very happy",
  "I hate fake friendships",
  "I enjoy funny conversations",
  "I live in Bangalore",
  "Life feels overwhelming when expectations are too high",
  "Music makes my mood better",
  "I love coffee every morning",
  "I get upset when someone interrupts me",
  "I enjoy late-night talks",
  "I love playing cricket",
  "I don't like spicy food",
  "I get angry when people don't respect time",
  "I feel proud when I help others",
  "I hate dishonesty",
  "I enjoy exploring new restaurants",
  "I feel grateful for small things",
  "I love travelling to hill stations",
  "I get tired when I work without breaks",
  "I enjoy learning something new daily",
  "I live in Bangalore now",
  "I love movies that make me laugh",
  "I feel sad when my efforts are ignored",
  "I enjoy deep meaningful conversations",
  "I get excited when planning trips",
  "I hate being compared to others",
  "I love people with good sense of humor"
]
Use this file in the UI for your demo.

🧪 Tests
Create the folder tests and add:

tests/test_memory_extractor.py:

python

from app.memory_extractor import MemoryExtractor

def test_extraction():
    messages = [
        "I love travelling",
        "I feel sad sometimes",
        "My name is Rahul",
        "I live in Hyderabad"
    ]

    mem = MemoryExtractor().extract(messages)

    assert isinstance(mem, dict)
    assert "preferences" in mem
    assert "facts" in mem
    assert "emotional_patterns" in mem
    assert len(mem["preferences"]) >= 1
    assert len(mem["facts"]) >= 1
    assert len(mem["emotional_patterns"]) >= 1

if __name__ == "__main__":
    test_extraction()
    print("✔ Memory extractor test passed")
Run the test like this:

bash

venv\Scripts\activate
python tests/test_memory_extractor.py
🧠 What This Demonstrates (For Reviewers)
Reasoning & Prompt-less Heuristics
Memory extractor uses simple, interpretable rules over raw messages to infer:

preferences (likes/dislikes, style)

emotional patterns (positive / negative themes)

factual information (name, city, habits)

Structured Output Parsing
Memory is always returned as:

json

{
  "preferences": [...],
  "emotional_patterns": [...],
  "facts": [...]
}
Personality Engine
ResponseGenerator chooses persona based on memory:

More negative emotional patterns → therapist_style

Fun/travel/hobby-heavy preferences → witty_friend

Otherwise → calm_mentor

Then it generates both a neutral and a personality-aware answer for the same input.

Modular System Design

Extraction and response generation are separated (memory_extractor.py vs response_generator.py).

UI (main.py) just orchestrates them.
