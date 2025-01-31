import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()

ELEVEN_LAB_API=os.getenv("ELEVEN_LAB_API")

def google_text_to_speech(input_text, output_filepath):
    language = "en"

    # Generate audio using gTTS and export directly to WAV
    audio_obj = gTTS(text=input_text, lang=language, slow=False)
    temp_mp3 = "temp_audio.mp3"  # Temporary file for MP3
    audio_obj.save(temp_mp3)

    # Convert MP3 to WAV (directly save as output_filepath)
    AudioSegment.from_mp3(temp_mp3).export(output_filepath, format="wav")

    # Remove the temporary MP3 file
    try:
        import os
        os.remove(temp_mp3)
    except Exception as e:
        print(f"Could not remove temporary file: {e}")

    # Detect operating system and play the WAV audio
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


#google_text_to_speech("Hello, I am a text-to-speech bot", "output.wav")

def elevenlabs_text_to_speech(input_text, output_filepath):
    # Initialize ElevenLabs client
    #client = ElevenLabs(api_key=ELEVEN_LAB_API)
    client = ElevenLabs(api_key=os.getenv("ELEVEN_LAB_API"))

    audio_generator = client.generate(
        text=input_text,
        voice="Brian",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    # Save the MP3 audio temporarily
    temp_mp3 = "temp_elevenlabs_audio.mp3"
    with open(temp_mp3, "wb") as f:
        for chunk in audio_generator:
            f.write(chunk)

    # Convert MP3 to WAV and save as the output file
    AudioSegment.from_mp3(temp_mp3).export(output_filepath, format="wav")

    # Remove the temporary MP3 file
    try:
        os.remove(temp_mp3)
    except Exception as e:
        print(f"Could not remove temporary MP3 file: {e}")

    # Detect operating system and play the WAV audio
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

#elevenlabs_text_to_speech(input_text="Hello", output_filepath="elevenlabs_autoplay.wav")

