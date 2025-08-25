import youtube_transcript_api
print(youtube_transcript_api.__file__)
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


# Debug: List all attributes of YouTubeTranscriptApi
print("Attributes of YouTubeTranscriptApi:")
print(dir(YouTubeTranscriptApi))

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

video_id = "dQw4w9WgXcQ"

try:
    # Instantiate YouTubeTranscriptApi
    yt = YouTubeTranscriptApi()

    # List available transcripts
    transcripts = yt.list(video_id)
    print("Available transcripts:")
    for transcript in transcripts:
        print(f"- {transcript.language_code} (generated: {transcript.is_generated})")

    # Fetch English transcript (or auto-generated if available)
    transcript_list = yt.fetch(video_id, languages=["en", "en-US", "en-GB"])

    # Inspect the structure of the fetched objects
    print("\nInspecting fetched transcript structure:")
    for snippet in transcript_list:
        print(snippet)

    # Assuming 'text' is an attribute of the object, we try to access it differently
    transcript_text = " ".join([snippet.text for snippet in transcript_list])
    print("\nTranscript:\n", transcript_text[:1000])  # Show first 1000 characters

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
except Exception as e:
    print("Error:", e)



