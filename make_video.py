# from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import os

image_folder = "images"
audio_path = "ICC vs Pak.mp4"

# Load audio from mp4
audio = AudioFileClip(audio_path)

# Read images
images = sorted(os.listdir(image_folder))

clips = []
duration_per_image = audio.duration / len(images)

for img in images:
    img_path = os.path.join(image_folder, img)
    clip = ImageClip(img_path).with_duration(duration_per_image)
    clips.append(clip)

# Merge image clips
video = concatenate_videoclips(clips, method="compose")

# Attach audio
final = video.with_audio(audio)

# Export
final.write_videofile(
    "output.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("✅ output.mp4 created successfully")
