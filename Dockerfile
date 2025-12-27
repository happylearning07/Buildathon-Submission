# Use Python 3.11 on Linux
FROM python:3.11-slim

# Install system dependencies for audio and Pathway
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libasound2-dev \
    portaudio19-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Pathway and requirements
RUN pip install --no-cache-dir "pathway[xpack-llm]" groq elevenlabs gtts pydub speechrecognition requests

# Copy your code into the container
COPY . .

# Expose the Pathway port
EXPOSE 8000

# Run the backend
CMD ["python", "doctor_agent_pathway.py"]