# Facade Pattern Example in Python

"""
Facade Pattern

The Facade pattern provides a simplified interface to a complex subsystem.
It hides the complexities of the system and provides an interface to the client through which the client can access the system.

Real-life example:
Consider a home theater system with various components like DVD Player, Projector, and Sound System.
The Facade pattern can provide a simple interface to control all these components together.
"""

# Subsystem Classes
class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def play(self, movie):
        print(f"Playing '{movie}'")

    def stop(self):
        print("DVD Player has stopped playing")

    def off(self):
        print("DVD Player is off")

class Projector:
    def on(self):
        print("Projector is on")

    def set_input(self, input_source):
        print(f"Projector input set to {input_source}")

    def off(self):
        print("Projector is off")

class SoundSystem:
    def on(self):
        print("Sound system is on")

    def set_volume(self, level):
        print(f"Sound system volume set to {level}")

    def off(self):
        print("Sound system is off")

# Facade Class
class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.dvd_player.on()
        self.dvd_player.play(movie)
        self.projector.on()
        self.projector.set_input("DVD")
        self.sound_system.on()
        self.sound_system.set_volume(5)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd_player.stop()
        self.dvd_player.off()
        self.projector.off()
        self.sound_system.off()

# Usage
if __name__ == "__main__":
    # Instantiate subsystem components
    dvd_player = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()

    # Create the facade
    home_theater = HomeTheaterFacade(dvd_player, projector, sound_system)

    # Use the facade to control the subsystem
    home_theater.watch_movie("Inception")
    # ... enjoy the movie ...
    home_theater.end_movie()

    # Output:
    # Get ready to watch a movie...
    # DVD Player is on
    # Playing 'Inception'
    # Projector is on
    # Projector input set to DVD
    # Sound system is on
    # Sound system volume set to 5
    # Shutting movie theater down...
    # DVD Player has stopped playing
    # DVD Player is off
    # Projector is off
    # Sound system is off
