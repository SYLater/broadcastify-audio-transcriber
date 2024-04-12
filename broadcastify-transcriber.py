from pydub import AudioSegment
import pyaudio
import requests
import speech_recognition as sr
from io import BytesIO
import numpy as np

# Initialize recognizer and pyaudio
recognizer = sr.Recognizer()
p = pyaudio.PyAudio()

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 16384*3
print(CHUNK)

transcription_location = r"path/to/file"

# Create a new audio stream
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

# Create buffer
buffer = BytesIO()

# Open file for saving transcriptions
with open(transcription_location, "a") as transcription_file:
    
    # Stream URL
    stream_url = 'https://listen.broadcastify.com/8dycj19fr2xzvms.mp3?nc=30737&xan=xtf9912b41c'
    
    # Request the stream
    response = requests.get(stream_url, stream=True)
    response.raise_for_status()

    # Loop to capture and transcribe
    for chunk in response.iter_content(chunk_size=CHUNK):
        buffer.write(chunk)
        
        if buffer.tell() >= CHUNK:
            # Create an AudioSegment
            audio_segment = AudioSegment.from_mp3(BytesIO(buffer.getvalue()))
            
            # Normalize to mono and desired frame rate
            audio_segment = audio_segment.set_channels(1).set_frame_rate(RATE)
            
            # Convert to bytes
            byte_data = audio_segment.raw_data
            
            # Audio level visualization
            audio_data = np.frombuffer(byte_data, dtype=np.int16)
            level = np.abs(audio_data).mean()
            bars = int(level // 100)
            print("Audio Level: [" + "#" * bars + "-" * (50 - bars) + "]")
            
            # Play audio
            stream.write(byte_data)

            # Transcribe
            audio_data = sr.AudioData(byte_data, RATE, 2)
            try:
                text = recognizer.recognize_google(audio_data=audio_data)
                print("Transcribed text:", text)  # Debug message
                transcription_file.write(text + "\n")
                transcription_file.flush()  # Ensure data is written to file
            except sr.UnknownValueError:
                print("Could not understand audio")  # Debug message
            except sr.RequestError as e:
                print(f"Could not request results; {e}")  # Debug message

            
            # Clear buffer
            buffer.seek(0)
            buffer.truncate()

# Stop and close the stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
