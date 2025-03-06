import task2_class_hierarchy as pl

# Create instances
audio_player = pl.AudioPlayer("MyAudioPlayer")
video_player = pl.VideoPlayer("MyVideoPlayer")
dvd_player = pl.DVDPlayer("MyDVDPlayer", "Movie DVD")

# Test methods
audio_player.play()
audio_player.stop()

video_player.play()
video_player.stop()

dvd_player.play()
dvd_player.stop()
dvd_player.insert_dvd("New Movie")
dvd_player.play()
dvd_player.eject_dvd()








