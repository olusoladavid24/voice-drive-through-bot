# Voice Drive-Through Bot 🎙️

A real-time voice AI assistant for restaurant FAQs built with 
OpenAI Whisper and Gemini.

## How It Works
1. Customer speaks a question
2. Whisper converts speech to text
3. Gemini generates a natural drive-through response
4. Bot prints the answer

## Technologies Used
- Python 3.13
- OpenAI Whisper (speech to text)
- Google Gemini API (LLM)
- ffmpeg (audio processing)
- python-dotenv (secure API key management)

## What I Learned
- How real-time voice AI pipelines work end to end
- Tradeoffs between Whisper model sizes and accuracy
- How audio quality affects AI transcription in noisy environments
- Secure API key management using environment variables
- Debugging real world errors in AI systems

## Challenges
- Whisper mishearing domain specific food words like "burger"
- Configuring ffmpeg on Windows for audio processing
- Managing API quotas on free tier cloud services

## Setup
1. Clone the repo
2. Install dependencies: `pip install openai-whisper google-generativeai python-dotenv`
3. Install ffmpeg
4. Add your API key to `.env` file: `GEMINI_API_KEY=your-key`
5. Add audio file as `test.wav`
6. Run: `python bot.py`# voice-drive-through-bot
Voice AI assistant for restaurant FAQs using Whisper and GPT-4
