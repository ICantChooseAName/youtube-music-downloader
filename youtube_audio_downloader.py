#!/usr/bin/env python3
"""
YouTube Audio Downloader
Downloads audio from YouTube videos in the best quality available.
Supports individual URLs, lists of URLs, and Watch Later playlist.
"""

import os
import sys
import argparse
from pathlib import Path


def download_audio(urls, output_dir="downloads", format_preference="m4a", use_oauth=False, watch_later=False):
    """
    Download audio from YouTube videos.
    
    Args:
        urls: Single URL string or list of URL strings
        output_dir: Directory to save downloaded files
        format_preference: Preferred audio format ('m4a' or 'mp3')
        use_oauth: Whether to use OAuth for YouTube authentication
        watch_later: Whether to download Watch Later playlist
    """
    try:
        import yt_dlp
    except ImportError:
        print("ERROR: yt-dlp is not installed.")
        print("Install it with: pip install yt-dlp")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
    }
    
    # Audio format options
    if format_preference == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # Best quality MP3
        }]
    else:  # m4a (AAC) - typically better quality and smaller file size
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    
    # Add metadata
    ydl_opts['postprocessors'].append({
        'key': 'FFmpegMetadata',
        'add_metadata': True,
    })
    
    # OAuth authentication for accessing private playlists like Watch Later
    if use_oauth or watch_later:
        ydl_opts['username'] = 'oauth2'
        ydl_opts['password'] = ''
        print("\n⚠️  OAuth authentication will be required.")
        print("A browser window will open for you to log in to your YouTube account.\n")
    
    # Handle Watch Later playlist
    if watch_later:
        urls = ['https://www.youtube.com/playlist?list=WL']
        print("📺 Downloading from Watch Later playlist...\n")
    
    # Ensure urls is a list
    if isinstance(urls, str):
        urls = [urls]
    
    # Download each URL
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                print(f"\n{'='*60}")
                print(f"Processing: {url}")
                print(f"{'='*60}")
                ydl.download([url])
                print(f"✅ Successfully downloaded: {url}\n")
            except Exception as e:
                print(f"❌ Error downloading {url}: {str(e)}\n")
                continue
    
    print(f"\n{'='*60}")
    print(f"✅ Download complete! Files saved to: {os.path.abspath(output_dir)}")
    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Download audio from YouTube videos in the best quality available.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download single video
  python youtube_audio_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  
  # Download multiple videos
  python youtube_audio_downloader.py "URL1" "URL2" "URL3"
  
  # Download as MP3 instead of M4A
  python youtube_audio_downloader.py -f mp3 "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  
  # Download Watch Later playlist (requires login)
  python youtube_audio_downloader.py --watch-later
  
  # Specify custom output directory
  python youtube_audio_downloader.py -o ~/Music/YouTube "URL"
        """
    )
    
    parser.add_argument(
        'urls',
        nargs='*',
        help='YouTube URL(s) to download'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='downloads',
        help='Output directory for downloaded files (default: downloads)'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['m4a', 'mp3'],
        default='m4a',
        help='Audio format preference (default: m4a). M4A typically has better quality/size ratio.'
    )
    
    parser.add_argument(
        '--watch-later',
        action='store_true',
        help='Download all videos from your Watch Later playlist (requires OAuth login)'
    )
    
    parser.add_argument(
        '--oauth',
        action='store_true',
        help='Use OAuth authentication (required for private playlists)'
    )
    
    args = parser.parse_args()
    
    # Validate input
    if not args.urls and not args.watch_later:
        parser.print_help()
        print("\n❌ Error: Please provide at least one URL or use --watch-later flag")
        sys.exit(1)
    
    # Check if ffmpeg is available (required for audio extraction)
    try:
        import subprocess
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n⚠️  WARNING: ffmpeg not found!")
        print("ffmpeg is required for audio extraction.")
        print("\nInstall instructions:")
        print("  macOS:   brew install ffmpeg")
        print("  Ubuntu:  sudo apt install ffmpeg")
        print("  Windows: Download from https://ffmpeg.org/download.html\n")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    # Download audio
    download_audio(
        urls=args.urls,
        output_dir=args.output,
        format_preference=args.format,
        use_oauth=args.oauth,
        watch_later=args.watch_later
    )


if __name__ == '__main__':
    main()
