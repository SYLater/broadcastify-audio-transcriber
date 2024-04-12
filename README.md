# broadcastify-audio-transcriber

This Python script allows you to capture and transcribe audio from a live stream in real-time. It utilizes the `pydub` library for audio processing, `pyaudio` for audio playback, `requests` for streaming audio data, and `speech_recognition` for speech-to-text transcription.

## Features

- Captures audio from a live stream URL
- Processes audio in real-time using `pydub` and `pyaudio`
- Transcribes the captured audio using the Google Speech Recognition API
- Provides audio level visualization in the console
- Saves the transcribed text to a file

## Requirements

- Python 3.x
- `pydub` library
- `pyaudio` library
- `requests` library
- `speech_recognition` library
- `numpy` library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/SYLatere/broadcastify-audio-transcriber.git
   ```

2. Install the required libraries:
   ```
   pip install pydub pyaudio requests SpeechRecognition numpy
   ```

## Usage

1. Open the `audio_transcriber.py` script in a text editor.

2. Modify the `transcription_location` variable to specify the desired location for saving the transcription file.

3. Update the `stream_url` variable with the URL of the live audio stream you want to capture and transcribe.

4. Run the script:
   ```
   python audio_transcriber.py
   ```

5. The script will start capturing and transcribing the audio from the live stream. The transcribed text will be displayed in the console and saved to the specified file.

6. To stop the script, press `Ctrl+C` in the console.

## Customization

- You can adjust the audio parameters such as `FORMAT`, `CHANNELS`, `RATE`, and `CHUNK` according to your requirements.
- Modify the `stream_url` variable to capture audio from a different live stream.
- Customize the audio level visualization by modifying the `bars` calculation and the visualization characters.

## Limitations

- The accuracy of the transcription depends on the quality of the audio stream and the performance of the Google Speech Recognition API.
- The script may not handle network interruptions or stream disconnections gracefully. Additional error handling and reconnection logic may be required for production use.

## License

This project is licensed under the [MIT License](LICENSE).
