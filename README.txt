# TranscribblerApp

TranscribblerApp is a standalone speech‑to‑text and speaker‑diarisation tool packaged with PyInstaller. It uses Whisper for transcription and FFmpeg for audio processing. All paths in this document assume you have placed the following items in the same folder:

- TranscribblerApp.exe  
- config.ini  
- bin\ffmpeg.exe  
- models\ (your Whisper model files)  

## Running the Application

To transcribe an audio file, open a Command Prompt in this folder and run:

```bash
TranscribblerApp.exe --config config.ini input_audio.wav