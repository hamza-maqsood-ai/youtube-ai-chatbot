from youtube_transcript_api import YouTubeTranscriptApi

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ================================
# STEP 1 : Fetch Transcript
# ================================

video_id = "Gfr50f6ZBvo"

api = YouTubeTranscriptApi()

transcript_list = api.list(video_id)

transcript = transcript_list.find_generated_transcript(["en"]).fetch()

text = " ".join(chunk.text for chunk in transcript)

print("=" * 50)
print("Transcript Loaded Successfully")
print("=" * 50)


# ================================
# STEP 2 : Convert into Document
# ================================

doc = Document(page_content=text)

print("\nDocument Created Successfully")


# ================================
# STEP 3 : Split into Chunks
# ================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents([doc])

print(f"\nTotal Chunks : {len(chunks)}")


# ================================
# STEP 4 : Check First Chunk
# ================================

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

# =========================================
# STEP 5 : Load Embedding Model
# =========================================

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("\nEmbedding Model Loaded Successfully ✅")
# =========================================
# STEP 6 : Create FAISS Vector Database
# =========================================

from langchain_community.vectorstores import FAISS

vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embedding
)

# =========================================
# STEP 6 : Create FAISS Vector Database
# =========================================

from langchain_community.vectorstores import FAISS

vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embedding
)

print("\nFAISS Vector Database Created Successfully ✅")
# =========================================
# STEP 7 : Create Retriever
# =========================================

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

print("\nRetriever Created Successfully ✅")
# =========================================
# STEP 8 : Test Retriever
# =========================================

query = "Who is Demis Hassabis?"

retrieved_docs = retriever.invoke(query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(retrieved_docs, start=1):
    print("=" * 60)
    print(f"Chunk {i}")
    print("=" * 60)
    print(doc.page_content)
    print("\n")
# =========================================
# STEP 9 : Prompt Template
# =========================================

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="""
You are a helpful AI Assistant.

Answer ONLY from the provided transcript context.

If the answer is not available in the context,
just say:

"I don't know."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)

print("Prompt Template Created Successfully ✅")
# =========================================
# STEP 10 : Load Groq LLM
# =========================================

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    base_url="https://api.groq.com/openai/v1"
)

print("Groq LLM Loaded Successfully ✅")
# =========================================
# STEP 12 : Run LCEL Chain
# =========================================
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# Function to convert retrieved documents into one string
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Build LCEL Chain
chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

# Test Question
question = "Who is Demis Hassabis?"

response = chain.invoke(question)

print("\n==============================")
print("FINAL ANSWER")
print("==============================\n")

print(response)