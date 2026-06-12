# API Reference: AN/VQX-9 EGREGOROS

## Core Components

### 1. Cloud Proxy Interface (`src/proxy.py`)
- `synthesize(text, profile)`: Dispatches text to `edge-tts` using the specified behavioral profile.
- Return: Raw audio stream.

### 2. Local Manipulator (`src/manipulator.py`)
- `apply_filter(audio_stream, profile)`: Applies `pydub` filters based on the profile markers.
- Return: Processed audio file.

## Configuration
- `profiles/lancy_lough.json`: Behavioral markers for the Master Tattooist persona.
