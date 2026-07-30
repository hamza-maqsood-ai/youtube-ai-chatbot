<h1 align="center">🎥 YouTube RAG Chatbot</h1>

<p align="center">

Chat with <b>Any YouTube Video</b> using <b>AI</b> 🤖

</p>

<p align="center">

Built with ❤️ using LangChain • FAISS • Groq • Streamlit

</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit">

<img src="https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge">

<img src="https://img.shields.io/badge/FAISS-VectorDB-orange?style=for-the-badge">

<img src="https://img.shields.io/badge/Groq-Llama_3.3-purple?style=for-the-badge">

<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">

</p>
# ✨ Features

| Feature | Status |
|---------|--------|
| 🤖 AI Chatbot | ✅ |
| 🎥 Any YouTube Video | ✅ |
| 🌍 Multi Language | ✅ |
| 📚 RAG Pipeline | ✅ |
| 🔎 FAISS Search | ✅ |
| 🧠 HuggingFace Embeddings | ✅ |
| ⚡ Groq Llama 3.3 | ✅ |
| 💬 ChatGPT Style UI | ✅ |
| 📺 Thumbnail Preview | ✅ |
| 🔗 Multiple URL Support | ✅ |
---
# 🛠 Tech Stack

<p align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github" />

</p>

| Library | Purpose |
|----------|---------|
| Streamlit | Frontend |
| LangChain | RAG |
| FAISS | Vector Database |
| HuggingFace | Embeddings |
| Groq | LLM |
| YouTube Transcript API | Transcript |
User
   │
   ▼
YouTube URL
   │
   ▼
Transcript API
   │
   ▼
Document
   │
   ▼
Chunking
   │
   ▼
Embeddings
   │
   ▼
FAISS
   │
   ▼
Retriever
   │
   ▼
Groq LLM
   │
   ▼
Answer
# 📊 Project Highlights

- 🔥 Retrieval-Augmented Generation (RAG)

- 🎥 Works with Any YouTube Video

- 🌍 Supports Multiple Languages

- ⚡ Fast Responses with Groq

- 💬 ChatGPT Style Interface

- 📚 Built using LangChain
  # ⭐ If you like this project

Please consider giving this repository a ⭐

It helps support the project and motivates future updates.
# 🎥 YouTube RAG Chatbot

An AI-powered YouTube chatbot that allows users to ask questions about **any YouTube video** using **Retrieval-Augmented Generation (RAG)**.

Built with **LangChain**, **FAISS**, **Groq Llama 3.3**, **HuggingFace Embeddings**, and **Streamlit**.

---

## 📸 Preview

> 📷 ![App Screenshot](<img width="1366" height="641" alt="Screenshot (169)" src="https://github.com/user-attachments/assets/1582bf6d-ae81-4e0c-a836-71718a98be70" />
)

---

# ✨ Features

- 🎥 Chat with any YouTube video
- 🌍 Multi-language support
  - English
  - Urdu
  - Roman Urdu
  - Same as Question
- 🤖 AI-powered answers
- 📚 Retrieval-Augmented Generation (RAG)
- 🔎 FAISS Vector Search
- 🧠 HuggingFace Embeddings
- ⚡ Groq Llama 3.3 API
- 💬 ChatGPT-style interface
- 🖼 Video Thumbnail Preview
- 🔗 Supports multiple YouTube URL formats

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | Frontend |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| HuggingFace | Embeddings |
| Groq | LLM |
| YouTube Transcript API | Transcript Extraction |

---

# 📂 Project Structure

```
youtube-ai-chatbot/
│
├── app.py
├── rag.py
├── test.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── assets/
│
└── screenshots/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/hamza-maqsood-ai/youtube-ai-chatbot.git
```

Go to the project folder

```bash
cd youtube-ai-chatbot
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 💡 How It Works

1. User pastes a YouTube URL.
2. Transcript is extracted.
3. Transcript is split into chunks.
4. Chunks are converted into embeddings.
5. FAISS creates a vector database.
6. Relevant chunks are retrieved.
7. Groq LLM generates an answer.
8. Response is displayed in the selected language.

---

# 🌍 Supported Languages

- 🇬🇧 English
- 🇵🇰 Urdu
- 💬 Roman Urdu
- 🌐 Same as Question

---

# 📌 Future Improvements

- ✅ Streaming Responses
- ✅ Voice Chat
- ✅ Export Chat
- ✅ Conversation History
- ✅ Better ChatGPT UI
- ✅ Dark / Light Theme
- ✅ Multiple Video Support
- ✅ Caching
- ✅ Faster Retrieval

---

# 👨‍💻 Author

**Hamza Maqsood**

GitHub:

https://github.com/hamza-maqsood-ai

---

# ⭐ Support

If you like this project,

⭐ Star this repository

🍴 Fork it

🐞 Report Issues

💡 Suggest Improvements

---

# 📜 License

This project is licensed under the MIT License.
