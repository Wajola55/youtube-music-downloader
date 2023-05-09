### Youtube Music Downloader

<b>Command-Line and Graphical User Interfaces for Music Downloader</b>


![01 main](https://user-images.githubusercontent.com/118658753/236847484-289cbc49-6a81-4c5a-afbc-dcfef0578f95.png)

This repository features two user-friendly implementations of a music downloader application: a <b>Command-Line Interface (CLI)</b> and a <b>Graphical User Interface (GUI)</b>. Both implementations allow users to effortlessly download audio from YouTube videos.


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

After launching the GUI, input one or more YouTube video URLs (one per line), choose the desired audio format and quality, set the download directory, and click the "Download Audio" button. The progress of the downloads is conveniently displayed through a progress bar and a percentage label.
