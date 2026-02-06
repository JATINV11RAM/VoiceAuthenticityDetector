# API Documentation for Voice Authenticity Detector

## Overview
This document provides a comprehensive reference for the API endpoints available in the Voice Authenticity Detector. It includes information on request and response formats, classification meanings, audio requirements, and integration examples.

## Endpoints

### 1. **Analyze Voice**
- **URL:** `/api/analyze`
- **Method:** `POST`
- **Description:** Analyzes the audio input for authenticity.

#### Request Format:
```json
{
    "audio_file": "<base64_encoded_audio>",
    "language": "<language_code>"
}
```

#### Response Format:
```json
{
    "success": true,
    "message": "Analysis completed successfully.",
    "classification": "<classification>",
    "score": <score>
}
```

### 2. **Get Classification Meanings**
- **URL:** `/api/classification`
- **Method:** `GET`
- **Description:** Retrieves meanings for various classifications.

#### Response Format:
```json
{
    "classifications": [
        {
            "name": "real",
            "description": "Authentic voice"
        },
        {
            "name": "fake",
            "description": "Inauthentic or synthesized voice"
        }
    ]
}
```

## Classification Meanings
- **Real:** Indicates the voice is authentic.
- **Fake:** Indicates the voice has been manipulated or generated.

## Audio Requirements
- Audio format should be `WAV` or `MP3`.
- Sample rate should be at least `16 kHz`.
- Maximum file size should not exceed `10 MB`.

## Integration Examples

### Example 1: Analyzing a Voice
```javascript
const axios = require('axios');

const audioInput = '<base64_encoded_audio>';  // Replace with actual audio

axios.post('https://api.example.com/api/analyze', {
    audio_file: audioInput,
    language: 'en'
})
.then(response => {
    console.log('Analysis Result:', response.data);
})
.catch(error => {
    console.error('Error:', error);
});
```

### Example 2: Fetching Classification Meanings
```javascript
const axios = require('axios');

axios.get('https://api.example.com/api/classification')
.then(response => {
    console.log('Classification Meanings:', response.data);
})
.catch(error => {
    console.error('Error:', error);
});
```