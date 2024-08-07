import moviepy.editor  
from tkinter.filedialog import *


video = moviepy.editor.VideoFileClip("C:/Users/nimit/Downloads/4091133-hd_1280_720_30fps.mp4")
aud = video.audio
aud.write_audiofile("converted_audio.mp3")

print("Converted")