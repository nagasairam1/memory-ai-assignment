# GupShupp Assignment — Companion AI (Memory + Personality Engine)

This project demonstrates:
✔ Memory extraction from 30 chat messages  
✔ Personality-based response engine  
✔ Before/After tone transformation  

---

🔧 How to Run

1. Install dependencies: pip install -r requirements.txt
2.  Run app: streamlit run main.py  
3. Upload `chat_messages.json` (list of 30 user messages)
4. Type any prompt → see before/after personality change.

---
 📂 Project Structure
app/
memory_extractor.py
personality_engine.py
response_generator.py
utils.py
main.py
requirements.txt
README.md
.gitignore
sample_data/chat_messages.json
tests/test_memory_extractor.py

---

 ✨ Notes
- Pure local execution — no API keys needed
- No deployment required by user (matches assignment request)
- Personality selection is inferred from extracted user memory

---
📁 Folder: sample_data/

Create folder sample_data then add:

📄 sample_data/chat_messages.json
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


from app.memory_extractor import MemoryExtractor

messages = [
    "I love travelling",
    "I feel sad sometimes",
    "My name is Rahul",
    "I live in Hyderabad"
]

📁 Folder: tests/

Create folder tests then add:

📄 tests/test_memory_extractor.py

def test_extraction():
    mem = MemoryExtractor().extract(messages)
    assert len(mem["preferences"]) > 0
    assert len(mem["facts"]) > 0
    assert len(mem["emotional_patterns"]) > 0

print("✔ Memory extractor test passed")


Run:
streamlit run main.py


   
