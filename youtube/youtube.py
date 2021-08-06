import youtube_dl as you
# https://github.com/ytdl-org/youtube-dl
with you.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=KOlCfIR1t7c'])
