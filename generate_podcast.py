import os
import re
import tempfile
from google.cloud import texttospeech
from pydub import AudioSegment

TRANSCRIPT_FILE = "podcast_transcript.txt"
OUTPUT_FILE = "podcast_output.mp3"
VTT_FILE = "podcast_output.vtt"

VOICES = {
    "Tom": "en-AU-Chirp3-HD-Puck",
    "Bryan": "en-AU-Chirp3-HD-Charon",
}

PAUSE_BETWEEN_SEGMENTS_MS = 800


def parse_transcript(filepath):
    """Parse transcript into list of (speaker, text) tuples."""
    segments = []
    current_speaker = None
    current_text = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.rstrip("\n")

            # Check if line starts with a speaker label
            match = re.match(r"^(Tom|Bryan):\s*(.*)", line)
            if match:
                # Save previous segment if exists
                if current_speaker and current_text:
                    segments.append((current_speaker, " ".join(current_text)))
                current_speaker = match.group(1)
                current_text = [match.group(2)] if match.group(2) else []
            elif line.strip() == "":
                continue
            else:
                # Continuation line
                if current_speaker:
                    current_text.append(line.strip())

    # Don't forget the last segment
    if current_speaker and current_text:
        segments.append((current_speaker, " ".join(current_text)))

    return segments


def synthesise_segment(client, text, voice_name, output_path):
    """Synthesise a single text segment to an MP3 file."""
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-AU",
        name=voice_name,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config,
    )

    with open(output_path, "wb") as out:
        out.write(response.audio_content)


def format_vtt_time(ms):
    """Convert milliseconds to VTT timestamp format HH:MM:SS.mmm."""
    hours = int(ms // 3600000)
    minutes = int((ms % 3600000) // 60000)
    seconds = int((ms % 60000) // 1000)
    millis = int(ms % 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{millis:03d}"


def generate_vtt(segments_with_times, output_path):
    """Generate a VTT file from segments with timing info."""
    with open(output_path, "w") as f:
        f.write("WEBVTT\n\n")
        for i, (speaker, text, start_ms, end_ms) in enumerate(segments_with_times):
            f.write(f"{i+1}\n")
            f.write(f"{format_vtt_time(start_ms)} --> {format_vtt_time(end_ms)}\n")
            f.write(f"<v {speaker}>{text}\n\n")


def main():
    segments = parse_transcript(TRANSCRIPT_FILE)
    print(f"Parsed {len(segments)} segments from transcript")

    for i, (speaker, text) in enumerate(segments):
        preview = text[:80] + "..." if len(text) > 80 else text
        print(f"  [{i+1}] {speaker}: {preview}")

    client = texttospeech.TextToSpeechClient()
    combined = AudioSegment.empty()
    pause = AudioSegment.silent(duration=PAUSE_BETWEEN_SEGMENTS_MS)
    segments_with_times = []

    with tempfile.TemporaryDirectory() as tmpdir:
        for i, (speaker, text) in enumerate(segments):
            voice_name = VOICES[speaker]
            segment_path = os.path.join(tmpdir, f"segment_{i:03d}.mp3")

            print(f"Synthesising segment {i+1}/{len(segments)} ({speaker})...")
            synthesise_segment(client, text, voice_name, segment_path)

            segment_audio = AudioSegment.from_mp3(segment_path)

            start_ms = len(combined)
            if len(combined) > 0:
                combined += pause
                start_ms = len(combined)
            combined += segment_audio
            end_ms = len(combined)

            segments_with_times.append((speaker, text, start_ms, end_ms))

    combined.export(OUTPUT_FILE, format="mp3")
    generate_vtt(segments_with_times, VTT_FILE)

    duration_secs = len(combined) / 1000
    print(f"\nDone! Exported {OUTPUT_FILE} ({duration_secs:.1f}s)")
    print(f"VTT transcript written to {VTT_FILE}")


if __name__ == "__main__":
    main()
