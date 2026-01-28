from moviepy import (
    ImageClip,
    VideoFileClip,
    AudioFileClip,
    concatenate_videoclips,
    CompositeVideoClip
)
from moviepy.video.fx import FadeIn, FadeOut, Resize
import os

# ---------------- CONFIG ----------------
IMAGE_FOLDER = "images"
VIDEO_FOLDER = "videos"
AUDIO_PATH = "ICC vs Pak.mp4"
OUTPUT_FILE = "output.mp4"

WIDTH, HEIGHT = 1920, 1080
TRANSITION_DURATION = 0.5  # seconds
KEN_BURNS_ZOOM = 1.05      # 5% zoom
# ----------------------------------------

# ---------- KEN BURNS EFFECT ----------
def ken_burns(clip, zoom=1.05):
    return clip.resized(lambda t: 1 + (zoom - 1) * t / clip.duration)

# ---------- LOAD AUDIO ----------
audio = AudioFileClip(AUDIO_PATH)

image_clips = []
video_clips = []

# ---------- LIST FILES ----------
images = sorted([
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]) if os.path.isdir(IMAGE_FOLDER) else []

videos = sorted([
    f for f in os.listdir(VIDEO_FOLDER)
    if f.lower().endswith((".mp4", ".mov", ".avi"))
]) if os.path.isdir(VIDEO_FOLDER) else []

total_items = len(images) + len(videos)
if total_items == 0:
    raise RuntimeError("❌ No images or videos found")

# ---------- IMAGE CLIPS ----------
if images:
    duration_per_image = audio.duration / total_items

    for img in images:
        img_path = os.path.join(IMAGE_FOLDER, img)

        clip = ImageClip(img_path, duration=duration_per_image)

        # Resize to height and center
        clip = clip.with_effects([
            Resize(height=HEIGHT),
            FadeIn(TRANSITION_DURATION),
            FadeOut(TRANSITION_DURATION)
        ])

        clip = CompositeVideoClip(
            [clip.with_position("center")],
            size=(WIDTH, HEIGHT)
        )

        # Ken Burns zoom
        clip = ken_burns(clip, KEN_BURNS_ZOOM)

        image_clips.append(clip)

# ---------- VIDEO CLIPS (MUTED) ----------
for vid in videos:
    vid_path = os.path.join(VIDEO_FOLDER, vid)

    clip = VideoFileClip(vid_path).without_audio()

    clip = clip.with_effects([
        Resize(height=HEIGHT),
        FadeIn(TRANSITION_DURATION),
        FadeOut(TRANSITION_DURATION)
    ])

    clip = CompositeVideoClip(
        [clip.with_position("center")],
        size=(WIDTH, HEIGHT)
    )

    video_clips.append(clip)

# ---------- COMBINE ----------
all_clips = image_clips + video_clips

final_video = concatenate_videoclips(
    all_clips,
    method="compose",
    padding=-TRANSITION_DURATION
)

# ---------- AUDIO ----------
final_video = final_video.with_audio(audio)

# ---------- EXPORT ----------
final_video.write_videofile(
    OUTPUT_FILE,
    fps=24,
    codec="libx264",
    audio_codec="aac",
    threads=4
)

print("✅ Video created successfully (MoviePy 2.x compatible)")
