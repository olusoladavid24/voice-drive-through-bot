import whisper
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load your API key from .env file
load_dotenv()

# Step 1 - Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("small")
print("Model loaded!")

# Step 2 - Transcribe audio
print("Transcribing your question...")
result = model.transcribe("test.wav")
question = result["text"]
print(f"You asked: {question}")

# Step 3 - Send to Gemini for an answer
print("Getting answer from Gemini...")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

gemini = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="You are a friendly drive-through assistant. Answer customer questions in 1-2 sentences only."
)

response = gemini.generate_content(question)
answer = response.text
print(f"\nBot: {answer}")