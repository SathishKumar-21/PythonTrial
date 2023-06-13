albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

SONGS_LIST_INDEX = 3
SONGS_TITLE_INDEX = 1
while True:
    print("Please choose a album from below:")
    for index, (album, artist, year, songs) in enumerate(albums):
        print("{}:\t{}".format(index + 1, album))
    album_choice = int(input())
    if album_choice in range(1, len(albums)+1):
        songs_list = albums[album_choice-1][SONGS_LIST_INDEX]
        print("Please choose a song from below:")
        for i, song in songs_list:
            print("{}:\t{}".format(i, song))
        song_choice = int(input())
    else:
        break
    if song_choice in range(1, len(songs_list)+1):
        song = songs_list[song_choice - 1][SONGS_TITLE_INDEX]
        print("Playing: {}".format(song))
    print("=" * 80)
