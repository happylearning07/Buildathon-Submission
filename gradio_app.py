import gradio as gr
import os
import requests
from patient_voice import transcribe_with_groq
from doctor_voice import text_to_speech_with_elevenlabs

def process_inputs(image_filepath, audio_filepath, text_input, language):
    lang_map = {"en": "English", "hi": "Hindi", "es": "Spanish", "fr": "French", "de": "German"}
    target_language = lang_map.get(language, "English")

    # 1. Transcribe Voice (using your existing patient_voice logic)
    if audio_filepath:
        patient_query = transcribe_with_groq(
            stt_model="whisper-large-v3",
            audio_filepath=audio_filepath,
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            language=language
        )
    else:
        patient_query = text_input

    # 2. Query the Pathway Reactive Agent
    # We send the query + language instruction to the Pathway Server
    pathway_url = "http://127.0.0.1:8000/v1/retrieve"
    prompt = f"Patient says: {patient_query}. Respond as a professional doctor in {target_language}."
    
    try:
        response = requests.post(pathway_url, json={"query": prompt})
        doctor_response = response.json()["context"]
    except Exception as e:
        doctor_response = "Doctor is currently offline. Please check Pathway server."

    # 3. Generate Voice (using your existing doctor_voice logic)
    voice_path = text_to_speech_with_elevenlabs(doctor_response, "doctor_voice.mp3")
    
    return patient_query, doctor_response, voice_path

# --- GRADIO UI (Keep your theme as it was) ---
theme = gr.themes.Soft(primary_hue="teal", neutral_hue="slate")
with gr.Blocks(theme=theme, title="V.A.I.D. Pathway Edition") as demo:
    gr.Markdown("# 🏥 V.A.I.D. (Virtual AI Doctor)")
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="filepath", label="Scan Symptoms")
            language_dropdown = gr.Dropdown(choices=[("English", "en"), ("Hindi", "hi")], value="en")
            audio_input = gr.Audio(sources=["microphone"], type="filepath")
            text_input = gr.Textbox(placeholder="Or type here...")
            submit_btn = gr.Button("Consult V.A.I.D.", variant="primary")
        with gr.Column():
            input_transcript = gr.Textbox(label="You Said", interactive=False)
            doctor_text_output = gr.Textbox(label="Diagnosis", interactive=False)
            audio_output = gr.Audio(label="Doctor's Voice", autoplay=True)

    submit_btn.click(
        fn=process_inputs,
        inputs=[image_input, audio_input, text_input, language_dropdown],
        outputs=[input_transcript, doctor_text_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch()