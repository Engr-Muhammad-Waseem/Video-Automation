from moviepy import ImageClip, VideoFileClip, AudioFileClip, concatenate_videoclips
import os

# Folders
image_folder = "images"
video_folder = "videos"
audio_path = "ICC vs Pak.mp4"

# Load narration audio
audio = AudioFileClip(audio_path)

# --- Load images ---
images = sorted(os.listdir(image_folder))
image_clips = []
if images:
    # Total duration for each image
    duration_per_image = audio.duration / (len(images) + len(os.listdir(video_folder)))
    for img in images:
        img_path = os.path.join(image_folder, img)
        clip = ImageClip(img_path).with_duration(duration_per_image)
        image_clips.append(clip)

# --- Load video clips (mute them) ---
videos = sorted(os.listdir(video_folder))
video_clips = []
for vid in videos:
    vid_path = os.path.join(video_folder, vid)
    clip = VideoFileClip(vid_path).without_audio()  # <-- THIS REMOVES VIDEO AUDIO
    video_clips.append(clip)

# --- Combine images + muted videos ---
all_clips = image_clips + video_clips
final_video = concatenate_videoclips(all_clips, method="compose")

# --- Set narration as final audio ---
final_video = final_video.with_audio(audio)

# --- Export ---
final_video.write_videofile("output.mp4", fps=24, codec="libx264", audio_codec="aac")

print("✅ Video created successfully with images + muted video clips")
