import sys

from spotify import Song

if __name__ == '__main__':
    input_file = 'top50.csv'
    output_file = 'top50_mod.csv'
    relative_bpm = int(sys.argv[1])

    songs = Song.load_songs(input_file)

    for song in songs:
        song.change_speed(relative_bpm)

    Song.save_songs(songs, output_file)
