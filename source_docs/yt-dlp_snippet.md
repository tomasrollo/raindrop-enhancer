# How to download and extract Youtube video title and description using the yt-dlp library

```python
from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

video_title = None
video_description = None

with YoutubeDL() as ydl:
    info_dict = ydl.extract_info(url, download=False)
    video_title = info_dict.get('title', None)
    video_description = info_dict.get('description', None)
```