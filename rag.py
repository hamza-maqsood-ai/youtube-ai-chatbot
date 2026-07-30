from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
)

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


# ==========================================
# Convert Retrieved Documents into String
# ==========================================

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# ==========================================
# Get Transcript (Production Version)
# ==========================================

def get_transcript(video_id):

    api = YouTubeTranscriptApi()

    try:

        transcript_list = api.list(video_id)

        # --------------------------------------
        # Try English / Hindi / Urdu First
        # --------------------------------------

        preferred_languages = [
            "en",
            "hi",
            "ur",
        ]

        try:

            transcript = transcript_list.find_transcript(
                preferred_languages
            )

            data = transcript.fetch()

            return " ".join(chunk.text for chunk in data)

        except:

            pass

        # --------------------------------------
        # Otherwise Use First Available Transcript
        # --------------------------------------

        for transcript in transcript_list:

            try:

                data = transcript.fetch()

                return " ".join(chunk.text for chunk in data)

            except:

                continue

        raise Exception("Transcript Found But Could Not Be Read.")

    except TranscriptsDisabled:

        raise Exception(
            "This video has disabled subtitles."
        )

    except NoTranscriptFound:

        raise Exception(
            "No transcript available for this video."
        )

    except Exception as e:

        raise Exception(str(e))


# ==========================================
# Main Function
# ==========================================

def create_rag(video_id):

    # -----------------------------
    # STEP 1
    # -----------------------------

    text = get_transcript(video_id)

    # -----------------------------
    # STEP 2
    # -----------------------------

    document = Document(
        page_content=text
    )

    # -----------------------------
    # STEP 3
    # -----------------------------

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        [document]
    )

    # -----------------------------
    # STEP 4
    # -----------------------------

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # -----------------------------
    # STEP 5
    # -----------------------------

    vector_store = FAISS.from_documents(
        chunks,
        embedding
    )

    # -----------------------------
    # STEP 6
    # -----------------------------

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 4
        }
    )
    # ================================
    # STEP 7 : Prompt Template
    # ================================

    prompt = PromptTemplate(
        template="""
You are an intelligent YouTube AI Assistant.

Your job is to answer questions ONLY from the transcript provided below.

If the answer cannot be found in the transcript, reply ONLY:

"I don't know based on this video's transcript."

Never make up information.

-----------------------------------
Answer Language
-----------------------------------

Respond ONLY in this language:

{language}

Rules:

- English → Respond in English.
- Hindi → Respond in Hindi (Devanagari).
- Urdu → Respond in Urdu script.
- Roman Urdu → Respond in Roman Urdu.
- Same as Question → Detect the user's language automatically.

Even if the transcript is in another language,
understand it and answer in the requested language.

-----------------------------------
Transcript
-----------------------------------

{context}

-----------------------------------
Question
-----------------------------------

{question}

-----------------------------------
Answer
-----------------------------------
""",
        input_variables=[
            "context",
            "question",
            "language"
        ]
    )

    # ================================
    # STEP 8 : Load Environment
    # ================================

    load_dotenv()

    # ================================
    # STEP 9 : LLM
    # ================================

    llm = ChatOpenAI(
        model="llama-3.3-70b-versatile",
        base_url="https://api.groq.com/openai/v1",
        temperature=0
    )

    # ================================
    # STEP 10 : LCEL Chain
    # ================================

    chain = (
        {
            "context": lambda x: format_docs(
                retriever.invoke(x["question"])
            ),
            "question": lambda x: x["question"],
            "language": lambda x: x["language"]
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain