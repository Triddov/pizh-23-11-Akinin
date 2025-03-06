## Overview
This module provides a class hierarchy for different types of media players, including audio players, video players, and DVD players. The base class `Player` defines common functionalities, which are then extended by subclasses with specific behaviors.

---

## Classes and Methods

### `Player`
**Base class representing a generic media player.**

#### Attributes:
- `name` (str): Public attribute representing the name of the player.
- `_status` (str): Protected attribute indicating the player's status (e.g., "Playing", "Stopped").
- `__volume` (int): Private attribute representing the volume level.

#### Methods:
- `play() -> None`: Starts playing media and updates the status.
- `stop() -> None`: Stops playing media and updates the status.
- `_change_status(status: str) -> None`: Protected method to update the status.
- `__adjust_volume(level: int) -> None`: Private method to adjust the volume level.

---

### `AudioPlayer`
**Class representing an audio player, inheriting from `Player`.**

#### Methods:
- `play() -> None`: Starts audio playback and updates the status.
- `stop() -> None`: Stops audio playback and updates the status.

---

### `VideoPlayer`
**Class representing a video player, inheriting from `Player`.**

#### Methods:
- `play() -> None`: Starts video playback and updates the status.
- `stop() -> None`: Stops video playback and updates the status.

---

### `DVDPlayer`
**Class representing a DVD player, inheriting from `VideoPlayer`.**

#### Attributes:
- `_dvd` (str): Protected attribute storing the currently inserted DVD.
- `_current_position` (int): Protected attribute tracking the playback position.

#### Methods:
- `play() -> None`: Starts DVD playback from the current position.
- `stop() -> None`: Stops DVD playback and records the current position.
- `insert_dvd(dvd: str) -> None`: Inserts a new DVD and resets the position.
- `eject_dvd() -> None`: Ejects the current DVD and resets the position.

---
