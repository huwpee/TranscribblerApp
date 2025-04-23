# CHANGELOG

All notable changes to this project are documented in this file in accordance with “Keep a Changelog” guidelines.

## [1.0.0] – 2025‑04‑23

The first stable release of TranscribblerApp delivers a fully packaged Windows installer that integrates OpenAI’s Whisper transcription engine with the Pyannote speaker‑diarisation pipeline into a single, command‑line tool. The installer places the application under `C:\Program Files\TranscribblerApp`, bundles the FFmpeg binary and appends its folder to the system PATH, and creates Start‑menu and desktop shortcuts before validating the installation with a built‑in `--help` check. Users must supply their own Hugging Face access token to download the `pyannote/speaker‑diarization` model, and instructions for generating and persisting the token via PowerShell are included in the documentation. All necessary runtime hooks, patches and dependency assets are packaged so that no separate Python or FFmpeg installation is required. Subsequent runs reuse the locally cached diarisation model and do not require network access.  