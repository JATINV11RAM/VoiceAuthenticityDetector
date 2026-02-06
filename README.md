# Voice Authenticity Detector

## Project Overview
The Voice Authenticity Detector is a cutting-edge application designed to analyze audio samples and determine their authenticity. It utilizes advanced machine learning algorithms to differentiate between genuine and manipulated sounds.

## Features
- **Real-time Voice Analysis**: Analyze audio inputs in real-time for immediate feedback.
- **Multiple Audio Formats**: Supports various audio formats including MP3, WAV, and more.
- **Machine Learning**: Utilizes trained models for accurate detection of voice authenticity.
- **User-friendly Interface**: Intuitive UI for ease of use.

## Quick Start Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/JATINV11RAM/VoiceAuthenticityDetector.git
   cd VoiceAuthenticityDetector
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python app.py
   ```

## API Usage Examples
- **Checking Voice Authenticity**:
   - Endpoint: `/api/check_authenticity`
   - Method: `POST`
   - Request Body:
     ```json
     { "audio_file": "path/to/audio/file.wav" }
     ```
   - Response:
     ```json
     { "is_authentic": true, "confidence": 95.5 }
     ```

## Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow, Scikit-learn
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

## Deployment Guide
1. **Set up the environment**: Ensure Python 3.x is installed on your server.
2. **Clone the repository on your server**.
3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations** (if applicable).
5. **Start the application** using a WSGI server like Gunicorn or uWSGI for production.

## License
This project is licensed under the MIT License.