# import os
# import gradio as gr
# from dotenv import load_dotenv
# from model import encode_image, analyze_image
# from user_voice import record_audio, transcribe_audio
# from text_to_speech import google_text_to_speech, elevenlabs_text_to_speech

# load_dotenv()

# system_prompt = """You are a professional doctor providing a medical consultation based on an image and patient description. Your task is to analyze the image for any medical abnormalities and provide a concise, professional diagnosis or opinion. Follow these guidelines:

# 1. **Tone and Style**:
#    - Respond as if you are speaking directly to the patient in a clinical setting.
#    - Use empathetic and professional language, avoiding robotic or overly technical phrasing.
#    - Do not refer to yourself as an AI or mention that this is for learning purposes.

# 2. **Diagnosis and Analysis**:
#    - Begin your response immediately without preamble (e.g., "Based on what I see...").
#    - Focus on identifying potential medical issues in the image. If no issues are apparent, state that clearly.
#    - Provide a differential diagnosis if applicable, but keep it concise (1-2 possibilities).
#    - Suggest simple remedies or next steps (e.g., "I recommend consulting a specialist for further evaluation" or "You may benefit from...").

# 3. **Formatting**:
#    - Respond in a single, concise paragraph (2-3 sentences maximum).
#    - Avoid bullet points, numbered lists, or markdown formatting.
#    - Do not use phrases like "In the image, I see..." or "The image shows...". Instead, phrase it as if you are observing the patient directly (e.g., "With what I see, I think you have...").

# 4. **Limitations**:
#    - If the image is unclear or insufficient for a diagnosis, state that clearly and recommend further evaluation.
#    - Do not make definitive claims without sufficient evidence. Use phrases like "It appears..." or "This could indicate...".

# 5. **Example Response**:
#    - "With what I see, I think you may have a mild skin irritation. I recommend keeping the area clean and applying a soothing ointment. If the condition persists, consult a dermatologist for further evaluation."
# """


# def process_inputs(audio_filepath, image_filepath):
#     speech_to_text_output = transcribe_audio(GROQ_API_KEY=os.getenv("GROQ_API_KEY"), 
#                                                  audio_filepath=audio_filepath,
#                                                  stt_model="whisper-large-v3")

#     if image_filepath:
#         doctor_response = analyze_image(prompt=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="llama-3.2-11b-vision-preview")
#     else:
#         doctor_response = "No image provided for me to analyze"

#     voice_of_doctor = elevenlabs_text_to_speech(input_text=doctor_response, output_filepath="final.mp3") 

#     return speech_to_text_output, doctor_response, voice_of_doctor


# iface = gr.Interface(
#     fn=process_inputs,
#     inputs=[
#         gr.Audio(sources=["microphone"], type="filepath"),
#         gr.Image(type="filepath")
#     ],
#     outputs=[
#         gr.Textbox(label="Speech to Text"),
#         gr.Textbox(label="Doctor's Response"),
#         gr.Audio("Temp.mp3")
#     ],
#     title="AI Medical Consultation ",
# )

# iface.launch(debug=True)

















# import os
# import gradio as gr
# from dotenv import load_dotenv
# from model import encode_image, analyze_image
# from user_voice import record_audio, transcribe_audio
# from text_to_speech import google_text_to_speech, elevenlabs_text_to_speech

# # Load environment variables
# load_dotenv()

# system_prompt = """You are a professional doctor providing a medical consultation based on an image and patient description. Your task is to analyze the image for any medical abnormalities and provide a concise, professional diagnosis or opinion. Follow these guidelines:

# 1. **Tone and Style**:
#    - Respond as if you are speaking directly to the patient in a clinical setting.
#    - Use empathetic and professional language, avoiding robotic or overly technical phrasing.
#    - Do not refer to yourself as an AI or mention that this is for learning purposes.

# 2. **Diagnosis and Analysis**:
#    - Begin your response immediately without preamble (e.g., "Based on what I see...").
#    - Focus on identifying potential medical issues in the image. If no issues are apparent, state that clearly.
#    - Provide a differential diagnosis if applicable, but keep it concise (1-2 possibilities).
#    - Suggest simple remedies or next steps (e.g., "I recommend consulting a specialist for further evaluation" or "You may benefit from...").

# 3. **Formatting**:
#    - Respond in a single, concise paragraph (2-3 sentences maximum).
#    - Avoid bullet points, numbered lists, or markdown formatting.
#    - Do not use phrases like "In the image, I see..." or "The image shows...". Instead, phrase it as if you are observing the patient directly (e.g., "With what I see, I think you have...").

# 4. **Limitations**:
#    - If the image is unclear or insufficient for a diagnosis, state that clearly and recommend further evaluation.
#    - Do not make definitive claims without sufficient evidence. Use phrases like "It appears..." or "This could indicate...".

# 5. **Example Response**:
#    - "With what I see, I think you may have a mild skin irritation. I recommend keeping the area clean and applying a soothing ointment. If the condition persists, consult a dermatologist for further evaluation."
# """

# class APIKeys:
#     def __init__(self):
#         self.groq_key = None
#         self.eleven_labs_key = None

# api_keys = APIKeys()

# def save_api_keys(groq_key, eleven_labs_key):
#     api_keys.groq_key = groq_key
#     api_keys.eleven_labs_key = eleven_labs_key
#     return gr.update(visible=False), gr.update(visible=True)

# def process_inputs(audio_filepath, image_filepath):
#     if not api_keys.groq_key or not api_keys.eleven_labs_key:
#         return "API keys not set", "Please set API keys first", None
    
#     speech_to_text_output = transcribe_audio(
#         GROQ_API_KEY=api_keys.groq_key,
#         audio_filepath=audio_filepath,
#         stt_model="whisper-large-v3"
#     )

#     if image_filepath:
#         doctor_response = analyze_image(
#             prompt=system_prompt + speech_to_text_output,
#             encoded_image=encode_image(image_filepath),
#             model="llama-3.2-11b-vision-preview"
#         )
#     else:
#         doctor_response = "No image provided for me to analyze"

#     voice_of_doctor = elevenlabs_text_to_speech(
#         input_text=doctor_response,
#         output_filepath="final.mp3"
#     )

#     return speech_to_text_output, doctor_response, voice_of_doctor

# with gr.Blocks() as app:
#     # API Keys Page
#     with gr.Group() as api_keys_page:
#         gr.Markdown("## Enter Your API Keys")
#         groq_key_input = gr.Textbox(
#             type="password",
#             label="Groq API Key",
#             placeholder="Enter your Groq API key"
#         )
#         eleven_labs_key_input = gr.Textbox(
#             type="password",
#             label="ElevenLabs API Key",
#             placeholder="Enter your ElevenLabs API key"
#         )
#         submit_button = gr.Button("Submit")

#     # Main Consultation Page
#     with gr.Group(visible=False) as main_page:
#         gr.Markdown("## AI Medical Consultation")
#         with gr.Row():
#             audio_input = gr.Audio(
#                 sources=["microphone"],
#                 type="filepath",
#                 label="Record Your Description"
#             )
#             image_input = gr.Image(
#                 type="filepath",
#                 label="Upload Medical Image"
#             )
        
#         with gr.Row():
#             text_output = gr.Textbox(label="Speech to Text")
#             response_output = gr.Textbox(label="Doctor's Response")
#             audio_output = gr.Audio(label="Doctor's Voice Response")

#     # Connect components
#     submit_button.click(
#         save_api_keys,
#         inputs=[groq_key_input, eleven_labs_key_input],
#         outputs=[api_keys_page, main_page]
#     )

#     inputs = [audio_input, image_input]
#     outputs = [text_output, response_output, audio_output]
    
#     audio_input.change(
#         process_inputs,
#         inputs=inputs,
#         outputs=outputs
#     )
#     image_input.change(
#         process_inputs,
#         inputs=inputs,
#         outputs=outputs
#     )

# if __name__ == "__main__":
#     app.launch(debug=True)




















































# import os
# import gradio as gr
# from dotenv import load_dotenv
# from model import encode_image, analyze_image
# from user_voice import record_audio, transcribe_audio
# from text_to_speech import google_text_to_speech, elevenlabs_text_to_speech

# # Load environment variables
# load_dotenv()

# system_prompt = """You are a professional doctor providing a medical consultation based on an image and patient description..."""  # Your existing prompt

# class APIKeys:
#     def __init__(self):
#         self.groq_key = None
#         self.eleven_labs_key = None

# api_keys = APIKeys()

# def save_api_keys(groq_key, eleven_labs_key):
#     api_keys.groq_key = groq_key
#     api_keys.eleven_labs_key = eleven_labs_key
#     return gr.update(visible=False), gr.update(visible=True)

# def process_inputs(audio_filepath, image_filepath):
#     if not api_keys.groq_key or not api_keys.eleven_labs_key:
#         return "API keys not set", "Please set API keys first", None
    
#     speech_to_text_output = transcribe_audio(
#         GROQ_API_KEY=api_keys.groq_key,
#         audio_filepath=audio_filepath,
#         stt_model="whisper-large-v3"
#     )

#     if image_filepath:
#         doctor_response = analyze_image(
#             prompt=system_prompt + speech_to_text_output,
#             encoded_image=encode_image(image_filepath),
#             model="llama-3.2-11b-vision-preview"
#         )
#     else:
#         doctor_response = "No image provided for me to analyze"

#     voice_of_doctor = elevenlabs_text_to_speech(
#         input_text=doctor_response,
#         output_filepath="final.mp3"
#     )

#     return speech_to_text_output, doctor_response, voice_of_doctor

# with gr.Blocks() as app:
#     # API Keys Page
#     with gr.Group() as api_keys_page:
#         gr.Markdown("## Enter Your API Keys")
#         groq_key_input = gr.Textbox(
#             type="password",
#             label="Groq API Key",
#             placeholder="Enter your Groq API key"
#         )
#         eleven_labs_key_input = gr.Textbox(
#             type="password",
#             label="ElevenLabs API Key",
#             placeholder="Enter your ElevenLabs API key"
#         )
#         submit_button = gr.Button("Submit")

#     # Main Consultation Page - Using original Interface layout
#     with gr.Group(visible=False) as main_page:
#         interface = gr.Interface(
#             fn=process_inputs,
#             inputs=[
#                 gr.Audio(sources=["microphone"], type="filepath"),
#                 gr.Image(type="filepath")
#             ],
#             outputs=[
#                 gr.Textbox(label="Speech to Text"),
#                 gr.Textbox(label="Doctor's Response"),
#                 gr.Audio("Temp.mp3")
#             ],
#             title="AI Medical Consultation",
#             allow_flagging="manual",
#             flagging_options=["Generated Output"]

#         )

#     # Connect components
#     submit_button.click(
#         save_api_keys,
#         inputs=[groq_key_input, eleven_labs_key_input],
#         outputs=[api_keys_page, main_page]
#     )

# if __name__ == "__main__":
#     app.launch(debug=True)



























import os
import gradio as gr
from dotenv import load_dotenv
from model import encode_image, analyze_image
from user_voice import record_audio, transcribe_audio
from text_to_speech import google_text_to_speech, elevenlabs_text_to_speech

load_dotenv()

system_prompt = """You are a professional doctor providing a medical consultation based on an image and patient description. Your task is to analyze the image for any medical abnormalities and provide a concise, professional diagnosis or opinion. Follow these guidelines:

1. **Tone and Style**:
   - Respond as if you are speaking directly to the patient in a clinical setting.
   - Use empathetic and professional language, avoiding robotic or overly technical phrasing.
   - Do not refer to yourself as an AI or mention that this is for learning purposes.

2. **Diagnosis and Analysis**:
   - Begin your response immediately without preamble (e.g., "Based on what I see...").
   - Focus on identifying potential medical issues in the image. If no issues are apparent, state that clearly.
   - Provide a differential diagnosis if applicable, but keep it concise (1-2 possibilities).
   - Suggest simple remedies or next steps (e.g., "I recommend consulting a specialist for further evaluation" or "You may benefit from...").

3. **Formatting**:
   - Respond in a single, concise paragraph (2 sentences maximum).
   - Avoid bullet points, numbered lists, or markdown formatting.
   - Do not use phrases like "In the image, I see..." or "The image shows...". Instead, phrase it as if you are observing the patient directly (e.g., "With what I see, I think you have...").

4. **Limitations**:
   - If the image is unclear or insufficient for a diagnosis, state that clearly and recommend further evaluation.
   - Do not make definitive claims without sufficient evidence. Use phrases like "It appears..." or "This could indicate...".
   - Respond with a maximum of 3 sentences.

5. **Example Response**:
   - "With what I see, I think you may have a mild skin irritation. I recommend keeping the area clean and applying a soothing ointment. If the condition persists, consult a dermatologist for further evaluation."
"""

class APIKeys:
    def __init__(self):
        self.groq_key = None
        self.eleven_labs_key = None

api_keys = APIKeys()

def save_api_keys(groq_key, eleven_labs_key):
    api_keys.groq_key = groq_key
    api_keys.eleven_labs_key = eleven_labs_key
    os.environ["GROQ_API_KEY"] = groq_key
    os.environ["ELEVEN_LAB_API"] = eleven_labs_key
    env_content = f"""GROQ_API_KEY = "{groq_key}"
    ELEVEN_LAB_API = "{eleven_labs_key}"
    """
    with open(".env", "w") as env_file:
        env_file.write(env_content)

    return gr.update(visible=False), gr.update(visible=True)

def process_inputs(audio_filepath, image_filepath):
    if not api_keys.groq_key or not api_keys.eleven_labs_key:
        return "API keys not set", "Please set API keys first", None
    
    speech_to_text_output = transcribe_audio(
        GROQ_API_KEY=api_keys.groq_key,
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    if image_filepath:
        doctor_response = analyze_image(
            prompt=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = elevenlabs_text_to_speech(
        input_text=doctor_response,
        output_filepath="final.mp3"
    )

    return speech_to_text_output, doctor_response, voice_of_doctor

with gr.Blocks() as app:
    # API Keys Page
    with gr.Group() as api_keys_page:
        gr.Markdown("## Enter Your API Keys")
        groq_key_input = gr.Textbox(
            type="password",
            label="Groq API Key",
            placeholder="Enter your Groq API key"
        )
        eleven_labs_key_input = gr.Textbox(
            type="password",
            label="ElevenLabs API Key",
            placeholder="Enter your ElevenLabs API key"
        )
        submit_button = gr.Button("Submit")

    # Main Consultation Page
    with gr.Group(visible=False) as main_page:
        with gr.Row():
            audio_input = gr.Audio(sources=["microphone"], type="filepath")
            image_input = gr.Image(type="filepath")
        
        with gr.Row():
            output_button = gr.Button("Submit")
            
        with gr.Row():
            speech_to_text_output = gr.Textbox(label="Speech to Text")
            doctor_response_output = gr.Textbox(label="Doctor's Response")
            audio_output = gr.Audio("Temp.mp3")

        output_button.click(
            fn=process_inputs,
            inputs=[audio_input, image_input],
            outputs=[speech_to_text_output, doctor_response_output, audio_output]
        )

    # Connect API key components
    submit_button.click(
        save_api_keys,
        inputs=[groq_key_input, eleven_labs_key_input],
        outputs=[api_keys_page, main_page]
    )

if __name__ == "__main__":
    app.launch(debug=True)
