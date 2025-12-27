
<img width="1894" height="878" alt="image" src="https://github.com/user-attachments/assets/3a8f7ea5-a81e-446c-9c2a-7fa1f34feeae" />

# V.A.I.D. (Virtual AI Doctor) - The Reactive Agent Edition

**V.A.I.D.** is a production-oriented medical AI agent designed to overcome the "static knowledge" limitations of traditional Transformers. Built for the **Synaptix Frontier AI Hackathon (Track 1)**, it utilizes the **Pathway Streaming Engine** to maintain a live, continuous-learning knowledge base that reacts to new medical data in real-time.

## 🏥 Project Overview
Traditional RAG pipelines suffer from "Stale Context"—where information added minutes ago is unknown to the LLM. V.A.I.D. solves this by treating medical memory as a flowing stream rather than a static database, allowing the agent to internalize patient history and new medical literature incrementally.

### Core Features
* **Reactive Document Indexing**: Automatically updates vector embeddings in milliseconds when new lab reports or notes are added to the knowledge base.
* **Multimodal Interaction**: Supports voice-to-text intake (Whisper-v3), vision-based symptom scanning, and human-like vocal feedback (ElevenLabs).
* **Post-Transformer Reasoning**: Powered by Llama-3.3 via Groq for ultra-low latency planning and multi-step medical reasoning.
* **Multilingual Support**: Provides expert-level healthcare assistance in multiple languages (Hindi/Spanish/English) to bridge rural accessibility gaps.

## 🛠️ Tech Stack
| Component | Technology Used |
| :--- | :--- |
| **Brain (LLM)** | Llama-3.3-70B (via Groq Cloud) |
| **Ears (STT)** | Whisper-Large-v3 (via Groq Cloud) |
| **Voice (TTS)** | ElevenLabs Multilingual v2 |
| **Reactive Core** | **Pathway Engine** |
| **Containerization** | Docker |
| **Frontend** | Gradio (Python) |

## 🚀 Getting Started

### 1. Prerequisites
* Docker Desktop installed and running.
* API Keys for Groq and ElevenLabs.

### 2. Environment Setup
Create a `.env` file in the root directory:
```bash
GROQ_API_KEY=your_groq_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```




### 3. Build & Run (Docker)
Build the reactive medical brain:
```bash
docker build -t medical-brain .
docker run -p 8000:8000 --env-file .env medical-brain
```

### 4. Run the frontend
```bash
python gradio_app.py
```

## 5.🔮 Future Roadmap: 
BDH IntegrationV.A.I.D. is designed to transition from RAG-based retrieval to Hebbian-based memory dynamics using the Dragon Hatchling (BDH) architecture

1. This shift will enable:Linear Attention $O(T)$: Reasoning across entire patient life histories without the quadratic memory ceiling of Transformers
   
2. Internalized Memory: Moving from "searching" to "remembering" via synaptic plasticity

### 6. Proposal Link
https://drive.google.com/file/d/1gmR0fbG1JWdgAN74dOFgA73q8aZGmOFi/view?usp=sharing

### 7. Video Link
https://drive.google.com/file/d/1FQF9b0WK9eF5Nn9mPyg_29YnLZ4yFfmi/view?usp=sharing
