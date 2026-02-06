# Setup Instructions for VoiceAuthenticityDetector

## Development Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JATINV11RAM/VoiceAuthenticityDetector.git
   cd VoiceAuthenticityDetector
   ```

2. **Install Docker**:
   - Follow the installation instructions for your operating system from [Docker's official website](https://docs.docker.com/get-docker/).

3. **Build the Docker Image**:
   ```bash
   docker build -t voice-authenticity-detector .
   ```

4. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 voice-authenticity-detector
   ```
   - Access the application at `http://localhost:5000`

## Production Deployment

1. **Pull the Docker Image** (if not built locally):
   ```bash
   docker pull yourusername/voice-authenticity-detector:latest
   ```

2. **Run the Docker Container** with Environment Variables:
   ```bash
   docker run -d -p 80:5000 \
      -e ENV=production \
      --name voice-authenticity-detector \
      yourusername/voice-authenticity-detector:latest
   ```

3. **Ensure your Docker service is running** and check your logs for any issues:
   ```bash
   docker logs voice-authenticity-detector
   ```

## Local Development Setup

This section details how to set up the project without Docker:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JATINV11RAM/VoiceAuthenticityDetector.git
   cd VoiceAuthenticityDetector
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   - Access the application at `http://localhost:5000`

## Conclusion
Follow the appropriate setup instructions based on your development or production needs. For further questions, please refer to the project's documentation or contact the maintainers.