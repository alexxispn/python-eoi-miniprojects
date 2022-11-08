from typing import List


class Song:
    def __init__(self, track: str, artist: str, genre: str, bpm: int,
                 energy: int, danceability: int, length: int):
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.energy = energy
        self.danceability = danceability
        self.length = length

    def __str__(self) -> str:
        return f'{self.track},{self.artist},{self.genre},{self.bpm},' \
               f'{self.energy},{self.danceability},{self.length}'

    def change_speed(self, relative_bpm: int) -> None:
        self.bpm += relative_bpm
        self.energy += (relative_bpm * 2)
        self.danceability += (relative_bpm * 3)
        self.length -= relative_bpm

    @staticmethod
    def load_songs(path: str) -> List['Song']:
        songs = []
        with open(path, 'r') as file:
            for line in file:
                track, artist, genre, bpm, energy, danceability, length = \
                    line.strip().split(',')
                songs.append(Song(track, artist, genre, int(bpm), int(energy),
                                  int(danceability), int(length)))
        return songs

    @staticmethod
    def save_songs(songs: List['Song'], path: str) -> None:
        with open(path, 'w') as file:
            for song in songs:
                file.write(str(song) + '\n')
