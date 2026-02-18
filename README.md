# YouTube Audio Downloader

A Python script to download audio from YouTube videos in the best quality available. Supports individual videos, batch downloads, and your YouTube Watch Later playlist.

## Features

- ✅ Download audio from single or multiple YouTube videos
- ✅ Download entire Watch Later playlist with browser cookies
- ✅ Choose between M4A (AAC) or MP3 format
- ✅ Best quality audio extraction
- ✅ Automatic metadata embedding
- ✅ Progress tracking and error handling

## Prerequisites

### 1. Python 3.7 or higher
Check your Python version:
```bash
python3 --version
```

### 2. FFmpeg (Required)
FFmpeg is needed to extract and convert audio.

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

**Verify installation:**
```bash
ffmpeg -version
```

## Installation

1. **Clone or download the script files**

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install yt-dlp
```

3. **Make the script executable (Linux/macOS):**
```bash
chmod +x youtube_audio_downloader.py
```

## Usage

### Basic Examples

**Download a single video:**
```bash
python youtube_audio_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Download multiple videos:**
```bash
python youtube_audio_downloader.py "URL1" "URL2" "URL3"
```

**Download as MP3 (instead of default M4A):**
```bash
python youtube_audio_downloader.py -f mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Specify custom output directory:**
```bash
python youtube_audio_downloader.py -o ~/Music/YouTube "VIDEO_URL"
```

**Download your entire Watch Later playlist (requires cookies):**
```bash
python youtube_audio_downloader.py --watch-later --cookies-from-browser chrome
```

### Command-Line Options

```
positional arguments:
  urls                  YouTube URL(s) to download

optional arguments:
  -h, --help           Show help message and exit
  -o, --output DIR     Output directory (default: downloads)
  -f, --format FORMAT  Audio format: m4a or mp3 (default: m4a)
  --watch-later        Download Watch Later playlist (requires --cookies-from-browser or --cookies)
  --cookies-from-browser
                       Browser to extract cookies from
  --cookies            Path to cookies.txt exported from your browser
```

## M4A vs MP3: Which Should You Choose?

**M4A (AAC) - Recommended ✅**
- Better quality at the same file size
- Native format for YouTube audio (no re-encoding)
- Smaller files with equivalent quality
- Widely supported by modern devices

**MP3**
- Universal compatibility
- Supported by older devices
- Slightly larger files for same quality
- Good choice for maximum compatibility

**Recommendation:** Use M4A (default) for best quality and file size. Only use MP3 if you need compatibility with older devices.

## Watch Later Playlist Authentication

To download your Watch Later playlist, you need to authenticate:

1. Log in to YouTube in your browser
2. Run the script with `--watch-later` and either `--cookies-from-browser` or `--cookies`
3. The script will use your browser cookies to access Watch Later

**Example:**
```bash
python youtube_audio_downloader.py --watch-later --cookies-from-browser chrome
```

Cookies are read from your local browser profile; nothing is uploaded.
Alternatively, export cookies to a file and pass `--cookies /path/to/cookies.txt`.

### Exporting Cookies (Safer Option)

You can export YouTube cookies to a `cookies.txt` file and pass it to the script:

```bash
python youtube_audio_downloader.py --watch-later --cookies ~/Downloads/youtube_cookies.txt
```

To export cookies, use a browser extension that exports in Netscape `cookies.txt` format (for example, “Get cookies.txt” for Chrome/Firefox). Store the file securely, and delete it when you’re done.

## Troubleshooting

### "yt-dlp is not installed"
```bash
pip install yt-dlp
```

### "ffmpeg not found"
Install ffmpeg using the instructions in the Prerequisites section.

### "ERROR: Video unavailable"
The video might be:
- Private or deleted
- Region-restricted
- Age-restricted (use `--cookies-from-browser` to access)

### Download is slow
This is normal - the script downloads the best quality available, which may be large files.

### Authentication issues with Watch Later
- Make sure you're using a Google account with an active YouTube account
- Try clearing browser cache and re-authenticating
- Check that your Watch Later playlist isn't empty

## Advanced Usage

### Batch download from a text file

Create a file `urls.txt` with one URL per line:
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3
```

Then use:
```bash
cat urls.txt | xargs python youtube_audio_downloader.py
```

Or modify the script to read from a file directly.

### Download playlists (other than Watch Later)

```bash
python youtube_audio_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

## Output

Downloaded files are saved as:
```
downloads/
├── Video Title 1.m4a
├── Video Title 2.m4a
└── Video Title 3.m4a
```

Files include embedded metadata (title, artist, album art when available).

## License

This script is for personal use only. Respect YouTube's Terms of Service and copyright laws.

## Notes

- Always respect content creators and copyright
- This tool is for backing up content you have permission to download
- YouTube's Terms of Service prohibit downloading content without permission
- Use responsibly and ethically
