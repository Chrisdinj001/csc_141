def make_album(artist, title):
    
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('mariah the scientist', 'love sick')
print(album)

album = make_album('summer walker', 'still over it')
print(album)

album = make_album('ariana grande', 'my everything')
print(album)