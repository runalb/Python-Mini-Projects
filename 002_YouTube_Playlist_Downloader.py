from pytube import Playlist
p = input("Enter th url of the playlist")
purl = Playlist(p)

print(f'Downloading: {p.title}')

for video in purl.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    
    print(f'Downloaded: {p.title}')
