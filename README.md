# TranscribblerApp

TranscribblerApp is a Windows command-line tool that performs speech-to-text transcription using OpenAI's Whisper and speaker diarisation with Pyannote. It ships as a standalone installer that bundles Python, Whisper, Pyannote, and all necessary patches and hooks. Note: FFmpeg is required but not included in the installer and must be downloaded separately.

## Installation

Download TranscribblerAppInstaller-1.0.0.exe from the project's GitHub Releases page and launch it with administrator privileges. By default, TranscribblerApp installs to:

C:\Program Files (x86)\TranscribblerApp

The installer creates Start-menu and desktop shortcuts, and then runs a final --help check to verify functionality.

## FFmpeg Installation

After installing TranscribblerApp:

1. Download FFmpeg from https://ffmpeg.org/download.html (Windows builds section)
2. Extract the zip file and locate ffmpeg.exe
3. Copy ffmpeg.exe to C:\Program Files (x86)\TranscribblerApp\
4. You may need to run File Explorer as administrator to copy to this location

## Hugging Face Access Token

Speaker diarisation relies on the pyannote/speaker-diarization model, which requires licence acceptance on Hugging Face and a valid access token. Sign in at https://huggingface.co, go to Settings → Access Tokens, generate a new token with read scope, and copy the hf_… string.

In PowerShell you can set this token for the current session by running:

$env:PYANNOTE_AUTH_TOKEN = "hf_your_generated_token"

Or make it permanent across sessions by running:

setx PYANNOTE_AUTH_TOKEN "hf_your_generated_token"

Then closing and reopening PowerShell. As an alternative you may supply the token directly on the command line with the --pyannote-token flag.

## Usage

Open PowerShell and invoke the application with your input WAV file, desired output CSV path, Whisper model name, compute device, and token. For example:

& "C:\Program Files (x86)\TranscribblerApp\TranscribblerApp.exe" `
  --input "C:\path\to\input.wav" `
  --output "C:\path\to\output.csv" `
  --whisper-model base.en `
  --device cpu `
  --pyannote-token $env:PYANNOTE_AUTH_TOKEN

This command transcribes the audio, assigns speaker labels to each segment, and writes a timestamped CSV with columns for start time, end time, speaker label and transcript text. On first run the diarisation model downloads to your user cache; subsequent runs reuse the local cache without requiring network access.

## Troubleshooting

If you see a "401 Unauthorized" error during diarisation, confirm that you have accepted the model licence on Hugging Face and that your PYANNOTE_AUTH_TOKEN environment variable is set correctly.

If you get a "FileNotFoundError" or FFmpeg cannot be found, verify that you've placed ffmpeg.exe in the correct location:

C:\Program Files (x86)\TranscribblerApp\ffmpeg.exe

If TranscribblerApp.exe cannot be found, try C:\Program Files (x86)\TranscribblerApp\TranscribblerApp.exe in PowerShell.

## Support

For bug reports, feature requests or documentation updates, open an issue on the TranscribblerApp GitHub repository. Contributions are welcome under the terms of the project licence.
