import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog, messagebox

def convert_to_audio():
    video_path = entry.get()
    try:
        video = mp.VideoFileClip(video_path)
        audio = video.audio
        audio_file = video_path.rsplit('.', 1)[0] + ".mp3"
        audio.write_audiofile(audio_file)
        messagebox.showinfo("Success", f"Audio file saved as {audio_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")])
    if file_path:
        entry.delete(0, END)
        entry.insert(0, file_path)


root = Tk()
root.title("Video to Audio Converter")


frame = Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = Label(frame, text="Select video file:")
label.grid(row=0, column=0, sticky=W)

entry = Entry(frame, width=50)
entry.grid(row=0, column=1, pady=5)

browse_button = Button(frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5)

convert_button = Button(frame, text="Convert to Audio", command=convert_to_audio)
convert_button.grid(row=1, columnspan=3, pady=10)


root.mainloop()