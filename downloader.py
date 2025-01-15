import yt_dlp

class MyLogger(object):
    def debug(self, msg):0
    def warning(self, msg):0
    def error(self, msg):print(ascii(msg))
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
ydl_opts = {
    '--playlist-start':0,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
done = [
    "https://youtu.be/tu4HfcmMn1E",
    "https://www.youtube.com/watch?v=TAhyZegVkhw&pp=ygUJZm9yIGV2aWd0",
    "https://www.youtube.com/watch?v=tbNlMtqrYS0&pp=ygUJNTAwIG1pbGVz",
    "https://www.youtube.com/watch?v=7hx4gdlfamo&pp=ygULdGhlIGdhbWJsZXI%3D",
    "https://www.youtube.com/watch?v=djV11Xbc914&pp=ygUKdGFrZSBvbiBtZQ%3D%3D",
    "https://www.youtube.com/watch?v=fB8TyLTD7EE&list=RDUc59ulnJI2o&index=3",
    "https://youtube.com/playlist?list=RDUc59ulnJI2o&playnext=1",
    "https://www.youtube.com/watch?v=CFlMy48ui9s&pp=ygUSZmx5IG1lIHRvIHRoZSBtb29u",
    "https://www.youtube.com/watch?v=fB8TyLTD7EE&list=RDMMfB8TyLTD7EE&start_radio=1",
    "https://www.youtube.com/watch?v=g_vLIAXurig&list=RDg_vLIAXurig&start_radio=1",
    "https://www.youtube.com/watch?v=aatr_2MstrI&list=RD4IefnBAiu64&index=20",
    "https://www.youtube.com/watch?v=0J2QdDbelmY&list=RDMM&index=10",
]
linksForDownload = [
    "https://www.youtube.com/watch?v=4IefnBAiu64&list=RD4IefnBAiu64&index=2",
]
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(list(set(linksForDownload).difference(done)))
