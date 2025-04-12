from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        return None

def fetch_transcript(video_url):
    video_id = get_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL"

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])

        notes = text.replace('\n', ' ').split('. ')
        notes = [note.strip().capitalize() + '.' for note in notes if note]

        return text, notes

    except Exception as e:
        return str(e), []


print("Enter your YouTube URL")
youtube_url =input()  
text, notes = fetch_transcript(youtube_url)

print("\n📝 Full Transcript:\n")
print(text)

print("\n📌 Structured Notes:\n")
for i, note in enumerate(notes, 1):
    print(f"{i}. {note}")
