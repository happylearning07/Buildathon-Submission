import pathway as pw
from pathway.xpacks.llm.vector_store import VectorStoreServer
from pathway.xpacks.llm.llms import GroqChat
from pathway.xpacks.llm.embedders import OpenAIEmbedder
import os

# Set your API Keys
os.environ["GROQ_API_KEY"] = "your_groq_key"
os.environ["OPENAI_API_KEY"] = "your_openai_key" # Required for Embeddings

def start_medical_engine():
    # 1. LIVE DATA INGESTION: Watch the folder for patient history or journals
    data_sources = pw.io.fs.read(
        "./medical_knowledge_base", 
        format="binary", 
        with_metadata=True
    )

    # 2. THE BRAIN: High-speed Groq Llama Model
    model = GroqChat(
        model="llama-3.3-70b-versatile",
        temperature=0.3
    )

    # 3. DYNAMIC MEMORY: Vector Store Server
    # This replaces static context with real-time reactive memory
    server = VectorStoreServer(
        data_sources,
        embedder=OpenAIEmbedder(),
        llm=model
    )

    print("🏥 Pathway Medical Engine running at http://127.0.0.1:8000")
    server.run_server(host="127.0.0.1", port=8000)

if __name__ == "__main__":
    if not os.path.exists("./medical_knowledge_base"):
        os.makedirs("./medical_knowledge_base")
    start_medical_engine()