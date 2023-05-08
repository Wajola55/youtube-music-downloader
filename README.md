### Youtube Music Downloader

<b>Command-Line and Graphical User Interfaces for Music Downloader</b>


![01 main](https://user-images.githubusercontent.com/118658753/236847484-289cbc49-6a81-4c5a-afbc-dcfef0578f95.png)

This repository contains two implementations of a music downloader: a <b>command-line interface (CLI)</b> and a <b>graphical user interface (GUI)</b>.

The <b>CLI implementation</b> is based on Python and uses the music_downloader library to download audio from YouTube videos. 
It requires the music_downloader and pytube libraries to be installed, which can be done by running the following command:

<pre><code>
pip install <span class="command">music_downloader</span> <span class="command">pytube</span>
</code></pre>


To download audio using the CLI, run the main.py file and enter the YouTube video URL when prompted.

The <b>GUI implementation</b> is based on Python and uses the music_downloader and tkinter libraries. 
It provides a modern and user-friendly interface for downloading audio from one or more YouTube videos. 
It also supports selecting the audio format, quality, and download directory.

To use the GUI, run the app.py file. It requires the music_downloader, tkinter, ttkthemes, and Pillow libraries to be installed, 
which can be done by running the following command:

<pre><code>
pip install <span class="command">music_downloader</span> <span class="command">tkinter</span> <span class="command">ttkthemes</span> <span class="command">Pillow</span>
</code></pre>

Once the GUI is launched, enter one or more YouTube video URLs (one per line), 
select the audio format and quality, choose the download directory, and click the "Download Audio" button. 
The progress of the downloads is displayed in a progress bar and a percentage label.
