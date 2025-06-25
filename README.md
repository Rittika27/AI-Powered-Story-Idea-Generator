# 🧠 AI-Powered Story Idea Generator

Generate unique and engaging story ideas using the power of OpenAI GPT-4! This app lets you choose a **genre**, **theme**, and **character types** to instantly get a creative writing prompt for your next novel, short story, or screenplay.

---

## 🚀 Features

- 🎭 Genre & Theme Selection  
- 👤 Custom Character Types  
- 🤖 GPT-4 Powered Prompt Generator  
- ✨ Instant story ideas  
- 🌐 Deployable on Render.com for free

---

## 🛠️ Setup & Deployment (Render)

1. **Upload to GitHub**
2. **Go to [https://render.com](https://render.com)** → New + → Web Service
3. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT`
4. Add Environment Variable:
   - `OPENAI_API_KEY = your-api-key-here`

✅ Done! You’ll get a public link like `https://story-generator.onrender.com`

---

## 🧪 Sample Prompt Output

> *In a magical kingdom torn by war, a rogue knight and an orphaned wizard uncover an ancient prophecy that could end the bloodshed—or start a darker era...*

---

## 📁 Files

| File              | Purpose                            |
|-------------------|------------------------------------|
| `app.py`          | Main Streamlit app code            |
| `requirements.txt`| Python dependencies                |
| `README.md`       | Project overview and setup guide   |

---

## 💡 Future Ideas

- Export prompts to Notion or PDF  
- Save previous prompts in history  
- Add plot twists or story endings  

---

## 📬 Contact

Made by Rittika.
