"""
Graphical user interface (GUI) for the music downloader using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox
from music_downloader.downloader import download_audio, is_valid_youtube_url

def on_download_button_click():
    video_urls = url_entry.get("1.0", tk.END)

    if not video_urls.strip():
        messagebox.showerror("Error", "Please enter one or more YouTube URLs.")
        return

    video_urls = [url.strip() for url in video_urls.split('\n') if url.strip()]

    errors = []
    for url in video_urls:
        try:
            download_audio(url)
        except Exception as e:
            errors.append((url, e))

    if errors:
        error_messages = "\n".join(f"Error downloading {url}: {error}" for url, error in errors)
        messagebox.showerror("Error", f"Download failed for the following URL(s):\n\n{error_messages}")
    else:
        messagebox.showinfo("Success", "Audio files downloaded successfully!")




def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

# Create the main window
root = tk.Tk()
root.title("Music Downloader")

# Create a label and entry for the video URLs
url_label = tk.Label(root, text="YouTube video URLs (one per line):")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Text(root, width=50, height=10, wrap=tk.NONE)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a context menu for the URL entry field
context_menu = tk.Menu(url_entry, tearoff=0)
context_menu.add_command(label="Copy", command=lambda: root.clipboard_append(url_entry.selection_get()))
context_menu.add_command(label="Paste", command=lambda: url_entry.insert(tk.INSERT, root.clipboard_get()))

# Bind the context menu to the right-click event
url_entry.bind("<Button-3>", show_context_menu)

# Create the download button
download_button = tk.Button(root, text="Download Audio", command=on_download_button_click)
download_button.grid(row=1, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()

