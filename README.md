name: Auto Video Generator
description: >
  Python script to automate video creation from images, video clips, and narration audio.
  Combines images and muted video clips, overlays narration, and exports a final MP4 video.

features:
  - Combine multiple images and video clips into a single video
  - Automatically set duration for images
  - Mute video clips so only narration audio plays
  - Export final video in MP4 format

folder_structure:
  auto-video-generator:
    images: "Folder for images (.png, .jpg)"
    videos: "Folder for short video clips (.mp4, .mov)"
    audio_mp4: "Narration audio file (audio.mp4)"
    make_video_py: "Main Python script"
    gitignore: "Ignore cache, output videos, and unnecessary files"

requirements:
  python: ">=3.10"
  libraries:
    - moviepy: "pip install moviepy"

usage:
  - step: "Place your images in the images/ folder"
  - step: "Place your short video clips in the videos/ folder"
  - step: "Add your narration audio as audio.mp4 in the root folder"
  - step: "Run the script"
  - command: "python make_video.py"
  - output: "output.mp4 with images + muted video clips + narration audio"

notes:
  - "Ensure folder and file names are exactly: images, videos, audio.mp4"
  - "Image duration is automatically calculated based on number of items"
  - "Video clips retain original duration but are muted"
  - "Output audio comes only from narration file"

future_improvements:
  - "Split video based on scr
