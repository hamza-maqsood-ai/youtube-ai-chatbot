# ============================================
# YouTube AI Pro
# ChatGPT Style Interface
# Part 1
# ============================================

import streamlit as st
from rag import create_rag

import re
import time

# ============================================
# Page Config
# ============================================

st.set_page_config(
    page_title="YouTube AI Pro",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# Session State
# ============================================

if "chain" not in st.session_state:
    st.session_state.chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "video_loaded" not in st.session_state:
    st.session_state.video_loaded = False

if "video_url" not in st.session_state:
    st.session_state.video_url = ""

if "video_id" not in st.session_state:
    st.session_state.video_id = ""

if "language" not in st.session_state:
    st.session_state.language = "English"

# ============================================
# Extract Video ID
# ============================================

def extract_video_id(url):

    patterns = [

        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",

        r"youtu\.be\/([0-9A-Za-z_-]{11})",

        r"youtube\.com\/shorts\/([0-9A-Za-z_-]{11})",

        r"youtube\.com\/embed\/([0-9A-Za-z_-]{11})",

    ]

    for pattern in patterns:

        match = re.search(pattern, url)

        if match:

            return match.group(1)

    return None


# ============================================
# Thumbnail URL
# ============================================

def get_thumbnail(video_id):

    return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"


# ============================================
# Custom CSS
# ============================================

st.markdown("""

<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{

padding-top:2rem;

padding-bottom:2rem;

padding-left:3rem;

padding-right:3rem;

}

.main-title{

font-size:42px;

font-weight:bold;

text-align:center;

margin-bottom:5px;

color:#FF4B4B;

}

.sub-title{

text-align:center;

font-size:18px;

color:#BFBFBF;

margin-bottom:30px;

}

.video-card{

background:#1E1E1E;

padding:20px;

border-radius:18px;

border:1px solid #333;

margin-bottom:20px;

}

.chat-box{

border-radius:15px;

padding:10px;

}

.stButton>button{

width:100%;

border-radius:10px;

height:45px;

font-weight:bold;

font-size:16px;

}

.stTextInput input{

border-radius:12px;

}

.stSelectbox div{

border-radius:12px;

}

</style>

""", unsafe_allow_html=True)

# ============================================
# Header
# ============================================

st.markdown(
    """
<div class="main-title">
🎥 YouTube AI Pro
</div>

<div class="sub-title">
Ask Anything About Any YouTube Video
</div>
""",
unsafe_allow_html=True
)
# ============================================
# Sidebar
# ============================================

with st.sidebar:

    st.markdown("## 🎥 Video Settings")

    video_url = st.text_input(
        "Paste YouTube URL",
        value=st.session_state.video_url,
        placeholder="https://www.youtube.com/watch?v=..."
    )

    language = st.selectbox(
        "Answer Language",
        [
            "English",
            "Hindi",
            "Urdu",
            "Roman Urdu",
            "Same as Question"
        ],
        index=[
            "English",
            "Hindi",
            "Urdu",
            "Roman Urdu",
            "Same as Question"
        ].index(st.session_state.language)
    )

    st.markdown("---")

    load_video = st.button(
        "🚀 Load Video",
        use_container_width=True
    )

    new_chat = st.button(
        "💬 New Chat",
        use_container_width=True
    )

    clear_chat = st.button(
        "🗑 Clear Chat",
        use_container_width=True
    )

    st.markdown("---")

    if st.session_state.video_loaded:

        st.success("✅ Video Loaded")

        st.info(f"Language : {st.session_state.language}")

    else:

        st.warning("No video loaded")

# ============================================
# New Chat
# ============================================

if new_chat:

    st.session_state.messages = []

    st.toast("New chat started!")

# ============================================
# Clear Chat
# ============================================

if clear_chat:

    st.session_state.messages = []

    st.session_state.chain = None

    st.session_state.video_loaded = False

    st.session_state.video_url = ""

    st.session_state.video_id = ""

    st.toast("Chat cleared successfully!")

    st.rerun()

# ============================================
# Load Video
# ============================================

if load_video:

    if video_url.strip() == "":

        st.error("Please paste a YouTube URL.")

        st.stop()

    video_id = extract_video_id(video_url)

    if video_id is None:

        st.error("Invalid YouTube URL.")

        st.stop()

    st.session_state.video_url = video_url

    st.session_state.video_id = video_id

    st.session_state.language = language

    status = st.status(
        "Loading Video...",
        expanded=True
    )

    try:

        status.write("📥 Reading transcript...")

        time.sleep(0.5)

        status.write("🧠 Creating AI brain...")

        chain = create_rag(video_id)

        st.session_state.chain = chain

        time.sleep(0.5)

        status.write("✅ Finished")

        status.update(
            label="Video Ready",
            state="complete"
        )

        st.session_state.video_loaded = True

        st.toast("Video loaded successfully!")

    except Exception as e:

        status.update(
            label="Loading Failed",
            state="error"
        )

        st.error(e)

        st.stop()

# ============================================
# Video Information Card
# ============================================

if st.session_state.video_loaded:

    left, right = st.columns([1, 2])

    with left:

        st.image(
            get_thumbnail(st.session_state.video_id),
            use_container_width=True
        )

    with right:

        st.markdown(
            """
<div class="video-card">

<h3>🎥 Video Ready</h3>

Your AI Assistant has successfully analysed
this YouTube video.

Ask anything about this video.

</div>
""",
            unsafe_allow_html=True
        )

        st.success("Ready to answer your questions!")

st.divider()
# ============================================
# Welcome Screen
# ============================================

if not st.session_state.video_loaded:

    st.markdown(
        """
        <div style='text-align:center;padding:60px;'>

        <h2>👋 Welcome to YouTube AI Pro</h2>

        <p style='font-size:18px;color:gray;'>

        Paste any YouTube URL from the sidebar and start chatting
        with the video.

        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================
# Chat History
# ============================================

if st.session_state.video_loaded:

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

# ============================================
# Chat Input
# ============================================

if st.session_state.video_loaded:

    question = st.chat_input(
        "Ask anything about this YouTube video..."
    )

    if question:

        # -----------------------------
        # Save User Message
        # -----------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        # -----------------------------
        # AI Message
        # -----------------------------

        with st.chat_message("assistant"):

            thinking = st.empty()

            thinking.markdown(
                """
🤖 **Thinking...**

- 📖 Reading transcript...
- 🔍 Searching relevant chunks...
- 🧠 Generating answer...
"""
            )

            try:

                answer = st.session_state.chain.invoke(
                    {
                        "question": question,
                        "language": st.session_state.language
                    }
                )

                thinking.empty()

                response_box = st.empty()

                response_box.markdown(answer)

            except Exception as e:

                thinking.empty()

                answer = f"❌ Error: {e}"

                response_box = st.empty()

                response_box.error(answer)

        # -----------------------------
        # Save AI Response
        # -----------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
# ============================================
# Footer
# ============================================

st.divider()

footer_left, footer_right = st.columns([4, 1])

with footer_left:

    st.caption("🎥 YouTube AI Pro | Powered by LangChain • Groq • Streamlit")

with footer_right:

    if st.session_state.video_loaded:
        st.success("🟢 Online")
    else:
        st.warning("🔴 Offline")

# ============================================
# Sidebar Information
# ============================================

with st.sidebar:

    st.markdown("---")

    st.markdown("### 📊 Session")

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    if st.session_state.video_loaded:

        st.metric(
            "Status",
            "Ready"
        )

        st.code(
            st.session_state.video_id,
            language=None
        )

    else:

        st.metric(
            "Status",
            "Waiting"
        )

# ============================================
# Empty Chat Hint
# ============================================

if (
    st.session_state.video_loaded
    and len(st.session_state.messages) == 0
):

    st.info(
        """
### 👋 Ready!

Try asking questions like:

• Summarize this video

• What is the main topic?

• Explain this like I'm 10 years old.

• What are the key points?

• Give me important timestamps.

• Who is the speaker?

• What are the conclusions?
"""
    )

# ============================================
# Auto Scroll
# ============================================

st.markdown(
    """
<script>

window.scrollTo(
0,
document.body.scrollHeight
);

</script>
""",
    unsafe_allow_html=True
)

# ============================================
# Success Toast
# ============================================

if (
    st.session_state.video_loaded
    and len(st.session_state.messages) == 1
):

    st.toast("🚀 Chat Started!")

# ============================================
# End
# ============================================