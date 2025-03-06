class Player:
    """
    Base class representing a generic media player.
    """

    def __init__(self, name: str):
        self.name: str = name  # Public attribute
        self._status: str = "Stopped"  # Protected attribute
        self.__volume: int = 50  # Private attribute (volume level)

    def play(self) -> None:
        """
        Start playing media.
        """
        self._status = "Playing"
        print(f"{self.name} is now playing.")

    def stop(self) -> None:
        """
        Stop playing media.
        """
        self._status = "Stopped"
        print(f"{self.name} has stopped playing.")

    def _change_status(self, status: str) -> None:
        """
        Protected method to update the status.
        """
        self._status = status

    def __adjust_volume(self, level: int) -> None:
        """
        Private method to adjust volume.
        """
        self.__volume = max(0, min(100, level))
        print(f"Volume set to {self.__volume}.")


class AudioPlayer(Player):
    """
    Class representing an audio player.
    """

    def play(self) -> None:
        print(f"{self.name}: Playing audio track...")
        self._change_status("Playing Audio")

    def stop(self) -> None:
        print(f"{self.name}: Audio playback stopped.")
        self._change_status("Stopped")


class VideoPlayer(Player):
    """
    Class representing a video player.
    """

    def play(self) -> None:
        print(f"{self.name}: Playing video...")
        self._change_status("Playing Video")

    def stop(self) -> None:
        print(f"{self.name}: Video playback stopped.")
        self._change_status("Stopped")


class DVDPlayer(VideoPlayer):
    """
    Class representing a DVD player.
    """

    def __init__(self, name: str, dvd: str = None):
        super().__init__(name)
        self._dvd: str = dvd  # Protected attribute for the current DVD
        self._current_position: int = 0  # Playback position

    def play(self) -> None:
        if self._dvd:
            print(f"{self.name}: Playing DVD '{self._dvd}' from position {self._current_position}...")
            self._change_status("Playing DVD")
        else:
            print(f"{self.name}: No DVD inserted.")

    def stop(self) -> None:
        print(f"{self.name}: DVD playback stopped at position {self._current_position}.")
        self._change_status("Stopped")
        self._current_position += 10  # Simulating playback progress

    def insert_dvd(self, dvd: str) -> None:
        """
        Insert a new DVD into the player.
        """
        self._dvd = dvd
        self._current_position = 0
        print(f"{self.name}: Inserted DVD '{dvd}'.")

    def eject_dvd(self) -> None:
        """
        Eject the current DVD.
        """
        print(f"{self.name}: Ejected DVD '{self._dvd}'.")
        self._dvd = None
        self._current_position = 0
