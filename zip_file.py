import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']

filename = 'album.csv'

with open(filename, 'w', encoding='utf-8',newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    for row in albums:
        zip_objects = zip(keys, row)
        # print(zip_objects)
        # for thing in zip(keys, row):
        #     print('\t', thing)
        albums_dict = dict(zip_objects)
        print(albums_dict)
        writer.writerow(albums_dict)
