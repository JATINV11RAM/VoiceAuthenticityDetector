from fastapi import FastAPI, HTTPException
import librosa
import numpy as np

app = FastAPI()

# Load your pre-trained model here
# e.g., model = load_model('path_to_model_file')

@app.post("/detect")
async def detect_voice(file: bytes):
    try:
        # Decode audio file
        audio, sr = librosa.load(file, sr=None)

        # Extract features
        features = extract_features(audio)

        # Perform classification
        prediction = classify(features)

        return {'prediction': prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def extract_features(audio):
    # Example feature extraction
    mfccs = librosa.feature.mfcc(y=audio, sr=22050, n_mfcc=13)
    return np.mean(mfccs, axis=1)

def classify(features):
    # Implement your classification logic here
    # e.g., prediction = model.predict(features)
    # For now, we'll return a dummy prediction
    return "voice_detected"  # or "voice_not_detected"