import sys

from spotify import Song

args = sys.argv[1:]
if len(args) < 1:
    print('Usage: python mod_bpm.py <10>')
    sys.exit(1)

if __name__ == '__main__':
    input_file = 'top50.csv'
    output_file = 'top50_mod.csv'
    relative_bpm = int(args[0])

    songs = Song.load_songs(input_file)

    for song in songs:
        song.change_speed(relative_bpm)

    Song.save_songs(songs, output_file)
