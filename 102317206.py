import sys
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment


def download_videos(singer, n):
    print("Downloading songs...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': False
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(f"ytsearch{n}:{singer}", download=True)


def convert_and_trim(duration):
    print("Trimming audio...")
    clips = []
    for file in os.listdir("downloads"):
        path = os.path.join("downloads", file)
        audio = AudioSegment.from_file(path)
        clip = audio[:duration * 1000]
        clips.append(clip)
    return clips


def merge_clips(clips, output):
    print("Merging...")
    final = AudioSegment.empty()
    for c in clips:
        final += c
    final.export(output, format="mp3")


def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFile>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        n = int(sys.argv[2])
        duration = int(sys.argv[3])
    except:
        print("Number of videos and duration must be integers.")
        sys.exit(1)

    output = sys.argv[4]

    if n <= 10 or duration <= 20:
        print("Number of videos must be > 10 and duration > 20.")
        sys.exit(1)

    os.makedirs("downloads", exist_ok=True)

    try:
        download_videos(singer, n)
        clips = convert_and_trim(duration)
        merge_clips(clips, output)
        print("Mashup created successfully!")
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
