# 🎥 YouTube Video Transcript & Notes Generator

This is a simple Python script that fetches the **transcript** of a YouTube video and **automatically creates structured notes** from it!

---

## 📋 Features

- Fetch the **full transcript** of any YouTube video (with subtitles enabled).
- Generate **clean, structured notes** from the transcript.
- Supports both full YouTube URLs and short `youtu.be` links.
- Easy-to-use terminal interface.

---

## 🚀 How to Run

1. **Clone the Repository**  
```bash
git clone https://github.com/your-username/youtube-transcript-notes.git
cd youtube-transcript-notes
```

2. **Install the Required Package**  
```bash
pip install youtube-transcript-api
```

3. **Run the Script**  
```bash
python transcript_notes.py
```

4. **Enter the YouTube Video URL** when prompted.

---

## 🛠️ Code Overview

```python
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    # Extracts video ID from full or short YouTube URL
    ...

def fetch_transcript(video_url):
    # Fetches the transcript and creates notes
    ...
```

The script will output:

- 📝 Full Transcript
- 📌 Structured Notes (each note is a clean point)

---

## 📎 Example Output

```bash
Enter your YouTube URL:
https://www.youtube.com/watch?v=dQw4w9WgXcQ

📝 Full Transcript:
Never gonna give you up never gonna let you down ...

📌 Structured Notes:
1. Never gonna give you up.
2. Never gonna let you down.
3. Never gonna run around and desert you.
...
```

---

## 🌟 Future Improvements

- Add option to **download transcript and notes as a text/PDF file**.
- Create a **GUI/HTML frontend** for uploading a YouTube link easily.
- Support **translation** of transcripts into different languages.

---
