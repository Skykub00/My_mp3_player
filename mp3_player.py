
from audioplayer import AudioPlayer
import os 
list_song = os.listdir("/home/sky/mp3_playlist")
print(list_song)
# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.

for i in list_song:
            print(i)
            AudioPlayer("/home/sky/mp3_playlist/"+i).play(block=True)

#AudioPlayer("/home/sky/mp3_playlist/"+list_song[0]).play(block=True)
