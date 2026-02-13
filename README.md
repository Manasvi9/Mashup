# Audio Mashup Generator

This project is a Flask-based web application that creates an audio mashup from songs of a given singer.

The system takes user input from a web form, downloads videos from YouTube, extracts audio, trims them to a fixed duration, merges them into one file, and prepares it for delivery.

---

## Features

- Input singer name
- Download multiple YouTube videos
- Convert video to audio
- Trim each audio to a fixed length
- Merge into one mashup file
- Create ZIP for delivery
- Email sending logic implemented (credentials removed for safety)

---

## Technologies Used

- Python
- Flask (Web framework)
- yt-dlp (YouTube downloading)
- pydub / moviepy (audio processing)
- ffmpeg

---

## Project Structure
- app.py -> Flask web server
- 102317206.py -> Mashup generation CLI program
- requirements.txt -> Python dependencies
- README.md -> Project documentation
  
---

## How to Run the Project

### 1. Install dependencies
- pip install -r requirements.txt


### 2. Run Flask server
- python app.py


### 3. Open in browser
- http://127.0.0.1:5000


---

## How It Works

1. User enters singer name, number of videos, duration, and email.
2. Web server triggers the mashup generator program.
3. Songs are downloaded.
4. Audio is extracted and trimmed.
5. Clips are merged into one MP3.
6. File is zipped.
7. Email sending logic can deliver the file.

---

## Security Note

For safety reasons, sender email credentials are not included in the repository.  
SMTP integration exists but requires valid configuration.

---




