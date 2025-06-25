
import streamlit as st
import openai
import os

# --- SET OPENAI API KEY ---
openai.api_key = st.secrets["openai_api_key"]

# --- TITLE ---
st.title("🧠 AI-Powered Story Idea Generator")
st.markdown("Generate unique and creative writing prompts using GPT-4 based on your selected genre, theme, and character types.")

# --- INPUT FIELDS ---
genre = st.selectbox("📚 Choose a Genre", ["Fantasy", "Mystery", "Sci-Fi", "Romance", "Thriller", "Historical"])
theme = st.selectbox("🎭 Choose a Theme", ["Redemption", "Survival", "Betrayal", "Love", "Courage", "Loss"])
characters = st.multiselect("👤 Select Character Types", ["Orphan", "Detective", "Alien", "Rebel", "Time Traveler", "Villain", "Wizard", "Knight"])

# --- PROMPT GENERATION FUNCTION ---
def generate_ai_prompt(genre, theme, characters):
    char_text = ", ".join(characters) if characters else "a mysterious character"
    prompt = (
        f"Generate a unique and engaging story idea in the {genre} genre. "
        f"The story should explore the theme of {theme} and include characters like {char_text}. "
        f"The idea should be suitable for a novel or short story."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative writing assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=300
    )
    return response['choices'][0]['message']['content'].strip()

# --- GENERATE BUTTON ---
if st.button("✨ Generate Story Idea"):
    if genre and theme:
        with st.spinner("Generating your story idea..."):
            result = generate_ai_prompt(genre, theme, characters)
            st.success("Here’s your AI-generated story idea:")
            st.write(result)
    else:
        st.warning("Please select genre and theme.")
