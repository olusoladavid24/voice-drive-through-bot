import whisper

# Step 1 - Load the Whisper model
# 'small' is a good balance of speed and accuracy
print("Loading Whisper model...")
model = whisper.load_model("small")
print("Model loaded successfully!")

# Step 2 - Transcribe an audio file
# We will record a real audio file in the next step
result = model.transcribe("test.wav")

# Step 3 - Print the transcription
print(f"You said: {result['text']}")