"""
Graphical user interface (GUI) for the music downloader using Tkinter.
"""

import tkinter as tk
import os
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from music_downloader.downloader import download_audio
from tkinter import filedialog
from PIL import ImageTk


def on_download_button_click():
    video_urls = url_entry.get("1.0", tk.END)
    audio_format = format_combobox.get()

    if not video_urls.strip():
        messagebox.showerror("Error", "Please enter one or more YouTube URLs.")
        return

    video_urls = [url.strip() for url in video_urls.split('\n') if url.strip()]

    errors = []
    total_videos = len(video_urls)
    completed_videos = 0

    for url in video_urls:
        try:
            download_audio(url, audio_format)
            completed_videos += 1
            progress = (completed_videos / total_videos) * 100
            progress_bar["value"] = progress
            progress_label["text"] = f"{progress:.0f}%"
            root.update_idletasks()
        except Exception as e:
            errors.append((url, e))

    progress_bar["value"] = 0
    progress_label["text"] = "0%"

    if errors:
        error_messages = "\n".join(f"Error downloading {url}: {error}" for url, error in errors)
        messagebox.showerror("Error", f"Download failed for the following URL(s):\n\n{error_messages}")
    else:
        messagebox.showinfo("Success", "Audio files downloaded successfully!")


def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

# Create the main window with a modern theme
root = ThemedTk(theme="arc")
root.title("Music Downloader")

style = ttk.Style(root)
bg_color = style.lookup('TLabel', 'background')

# Create a label and entry for the video URLs
url_label = ttk.Label(root, text="YouTube video URLs (one per line):", font=("Arial", 11, "bold"))
url_label.grid(row=0, column=0, padx=(30, 10), pady=(30, 10), sticky=tk.W)

url_entry = tk.Text(root, width=50, height=10, wrap=tk.NONE, bd=2, relief=tk.GROOVE, font=("Helvetica", 12))
url_entry.grid(row=0, column=1, padx=(10, 30), pady=(30, 10))


# Set the background color of the root and other elements
root.configure(bg=bg_color)
url_label.configure(background=bg_color)


# Create a context menu for the URL entry field
context_menu = tk.Menu(url_entry, tearoff=0)
context_menu.add_command(label="Copy", command=lambda: root.clipboard_append(url_entry.selection_get()))
context_menu.add_command(label="Paste", command=lambda: url_entry.insert(tk.INSERT, root.clipboard_get()))

# Bind the context menu to the right-click event
url_entry.bind("<Button-3>", show_context_menu)

# Create a frame at the bottom of the window
bottom_frame = ttk.Frame(root)
bottom_frame.grid(row=2, column=0, columnspan=2, padx=(20, 20), pady=(10, 20))

# Create a label and a combobox for selecting the audio format
format_label = ttk.Label(bottom_frame, text="Audio format:", font=("Arial", 11, "bold"), background=bg_color)
format_label.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)

format_combobox = ttk.Combobox(bottom_frame, values=("mp3", "wav", "ogg"), state="readonly", width=10)
format_combobox.set("mp3")
format_combobox.grid(row=0, column=1, padx=(0, 10), pady=(0, 10), sticky=tk.W)

# Create a label and a button for choosing the download directory
dir_label = ttk.Label(bottom_frame, text="Choose directory:", font=("Arial", 11, "bold"), background=bg_color)
dir_label.grid(row=0, column=2, padx=(10, 10), pady=(0, 10), sticky=tk.W)

def choose_directory():
    global download_directory  # Declare the variable as global to be accessible outside this function

    # Open the directory selection dialog and store the selected directory path
    selected_directory = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Download Directory")
    
    if selected_directory:  
        download_directory = selected_directory  
        dir_label_text.set(f"Directory: {download_directory}")  


# Modify the dir_label to use a variable for the text content
dir_label_text = tk.StringVar(value="Choose directory:")
dir_label = ttk.Label(bottom_frame, textvariable=dir_label_text, font=("Arial", 11, "bold"), background=bg_color)
dir_label.grid(row=0, column=2, padx=(10, 10), pady=(0, 10), sticky=tk.W)

# ...

# Initialize the download_directory variable
download_directory = os.getcwd()

dir_button = tk.Button(bottom_frame, text="Browse", command=choose_directory, bg="#94c180", activebackground="#3F9E45", bd=0, highlightthickness=0, font=("Arial", 11, "bold"))
dir_button.grid(row=0, column=3, padx=(0, 10), pady=(0, 10), sticky=tk.W)


# Create a label, a combobox, and an image label for selecting the quality
quality_label = ttk.Label(bottom_frame, text="Quality:", font=("Arial", 11, "bold"), background=bg_color)
quality_label.grid(row=0, column=4, padx=(10, 10), pady=(0, 10), sticky=tk.W)

quality_combobox = ttk.Combobox(bottom_frame, values=("Low", "Medium", "High"), state="readonly", width=10)
quality_combobox.set("Medium")
quality_combobox.grid(row=0, column=5, padx=(0, 10), pady=(0, 10), sticky=tk.W)

# Create the download button using a Tkinter Button widget
download_button = tk.Button(root, text="Download Audio", command=on_download_button_click, bg="#94c180", activebackground="#3F9E45", bd=0, highlightthickness=0, font=("Arial", 11, "bold"))
download_button.grid(row=1, column=0, columnspan=2, pady=10)


# Configure the style for the progress bar
style.configure("TProgressbar", troughcolor='gray', background='green', thickness=20)

# Add a progress bar below the download button
progress_bar = ttk.Progressbar(root, length=200, mode="determinate")
progress_bar.grid(row=3, column=0, columnspan=2, pady=(0, 10))

# Add a label to show the progress percentage
progress_label = ttk.Label(root, text="0%", font=("Arial", 11, "bold"), background=bg_color)
progress_label.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky=tk.E)

def update_progress(progress):
    if "total_bytes" not in progress:
        return

    downloaded = progress["downloaded_bytes"]
    total = progress["total_bytes"]
    percentage = int(downloaded / total * 100)
    progress_bar["value"] = percentage
    root.update_idletasks()

# Start the Tkinter event loop
root.mainloop()

