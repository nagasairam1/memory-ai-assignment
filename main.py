import streamlit as st
from app.utils import load_messages
from app.memory_extractor import MemoryExtractor
from app.response_generator import ResponseGenerator

st.set_page_config(page_title="GupShupp AI Assignment", layout="wide")

st.title("🧠 Companion AI — Memory & Personality Engine Demo")

uploaded = st.file_uploader(
    "Upload chat messages JSON file (array of 30 messages)",
    type=["json"]
)

# Stop early if no file yet
if uploaded is None:
    st.info("⬆️ Upload a JSON file with 30 messages to continue.")
    st.stop()

# Now it's safe to load
messages = load_messages(uploaded)

mem = MemoryExtractor().extract(messages)
st.subheader("🧩 Extracted Memory")
st.json(mem)

st.markdown("---")
st.subheader("💬 Test Personality Response Engine")

user_input = st.text_input("Enter a user message:", "")

if user_input.strip():
    res = ResponseGenerator().generate(user_input, mem)

    st.markdown("### 🔹 Before (Neutral Response)")
    st.info(res["before"])

    st.markdown("### 🔹 After (Personality-Aware Response)")
    st.success(res["after"])

    st.caption(f"Persona Mode → **{res['persona_mode']}**")
