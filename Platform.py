from album import Album
from artist import Artist
from song import Song


class Platform:
    def __init__(self):
        self.__artists = []

    def getArtists(self):
        return self.__artists

    def addArtists(self, *args):
        for artist in args:
            add = True
            for arti in self.__artists:
                if arti.getFirstName() == artist.getFirstName() and arti.getSecondName() == artist.getSecondName():
                    if arti.getBirthYear() == artist.getBirthYear():
                        add = False
            if add:
                self.__artists.append(artist)

    def getTopTrendingArtist(self):
        artist = self.__artists[0]
        total = self.__artists[0].totalLikes()
        for arti in self.__artists:
            if arti.totalLikes() > total:
                total = arti.totalLikes()
                artist = arti
        mytuple = (artist.getFirstName(), artist.getSecondName())
        return mytuple

    def getTopTrendingAlbum(self):
        setAlbums = set()
        for artist in self.__artists:
            for alb in artist.getAlbums():
               setAlbums.add(alb)
        albom = None
        maximal = None
        first = True
        if len(setAlbums) == 0:
            return None
        else:
            for alb in setAlbums:
                if first:
                    first = False
                    tot = 0
                    for song in alb.getSongs():
                        tot += song.getLikes()
                    albom = alb
                    maximal = tot
                else:
                    tot = 0
                    for song in alb.getSongs():
                        tot += song.getLikes()
                    if tot > maximal:
                        albom = alb
                        maximal = tot
        return albom.getTitle()

    def getTopTrendingSong(self):
        setSongs = set()
        for artist in self.__artists:
            for alb in artist.getAlbums():
                for song in alb.getSongs():
                    setSongs.add(song)
            for song in artist.getSingle():
                setSongs.add(song)
        topSong = None
        maximal = None
        first = True
        if len(setSongs) == 0:
            return None
        else:
            for song in setSongs:
                if first:
                    topSong = song
                    maximal = song.getLikes()
                    first = False
                else:
                    tot = song.getLikes()
                    if tot > maximal:
                        maximal = tot
                        topSong = song
        return topSong.getTitle()


    @staticmethod
    def loadFromFile(path):
        ListofArtists = []
        ListofAlbums = []
        file = open(path, 'r')
        listArtists = []
        str = ""
        singles = ""
        strng = ""
        fileStr = file.read()
        for chr in range(len(fileStr)):
            if fileStr[chr] == '#':
                listArtists.append(str)
                str = ""
            elif fileStr[chr] == ' ':
                bool = chr > 0 and (chr < len(fileStr)-1) and (ord(fileStr[chr-1]) > 122 or ord(fileStr[chr-1]) < 65)
                bool = bool or 90 < ord(fileStr[chr-1]) < 97
                if bool:
                    bool = bool and (ord(fileStr[chr+1]) > 122 or ord(fileStr[chr+1]) < 65)
                    bool = bool or 90 < ord(fileStr[chr+1]) < 97
                if not bool and fileStr[chr-1] != ' ':
                    str += fileStr[chr]
            elif fileStr[chr] != '\n':
                str += fileStr[chr]
        if len(str) > 0:
            listArtists.append(str)


        for str in listArtists:

            first = True
            second = True
            third = True
            album = False
            singl = False
            name = ""
            songs = ""
            surname = ""
            releaseYear = ""
            strg = ''
            brackets = 0
            singles = ""
            albm = ""
            stg = ""
            strng = ""
            FirstThree = False
            frst = True

            for chr in range(len(str)):
                stg += str[chr]

                if str[chr: chr + 8] == 'artists:':
                    chr += 9
                elif str[chr] == ',' and not FirstThree:
                    if first:
                        if stg[0:9] == "artists:{":
                            stg = stg[9:len(stg) - 1]
                        name = stg[0:len(stg) - 1]
                        stg = ""
                        first = False
                    elif second:
                        surname = stg[0:len(stg) - 1]
                        stg = ""
                        second = False
                    elif third:
                        releaseYear = stg[0:len(stg) - 1]
                        stg = ""
                        third = False
                        FirstThree = True
                    else:
                        strg += str[chr]

                elif ((chr + 6) < len(str) and str[chr:chr + 6] == "albums") or album:
                    album = True
                    strng += str[chr]

                    if len(strng) > 8 and brackets == 0:

                        album = False
                        albm = strng + '}'
                        brackets = 1
                    elif str[chr] == '{':
                        brackets += 1
                    elif str[chr] == '}':
                        brackets -= 1

                elif singl or (((chr + 7) <= (len(str) - 1)) and str[chr: chr + 7] == "singles"):
                    songs += str[chr]
                    singl = True
                    if str[chr] == '{':
                        brackets += 1
                    elif str[chr] == '}':
                        brackets -= 1
                        if brackets == 0:
                            singles = songs
                            brackets = 1
                            singl = False


            songs = songs[10:len(songs) - 1]
            if songs[len(songs) - 1] == '}':
                songs = songs[0:len(songs) - 1]
            lst = songs.split('|')
            songList = []
            for elem in lst:
                listofelem = elem.split(',')
                time = listofelem[1].split(' ')[0]
                song = Song(listofelem[0], int(listofelem[2]), float(time) * 60, int(listofelem[3]))
                songList.append(song)

            albm = albm[9:(len(albm) - 1)]

            albom = albm.split('%')


            ListofSongs = []
            for albomi in albom:
                lst = albomi.split('{')
                stringofalbum = lst[1][1:]
                lst1 = lst[0]
                lstofalbum = lst1.split(',')

                while stringofalbum[len(stringofalbum) - 1] == '}' or stringofalbum[len(stringofalbum) - 1] == ',':
                    stringofalbum = stringofalbum[:len(stringofalbum) - 1]

                lst = stringofalbum.split('|')
                musics = []

                for elem in lst:
                    listofelem = elem.split(',')

                    time = listofelem[1].split(' ')[0]
                    song = Song(listofelem[0], int(listofelem[2]), float(time) * 60, int(listofelem[3]))
                    musics.append(song)
                albomforlist = Album(lstofalbum[0], int(lstofalbum[1]))
                for song in musics:
                    albomforlist.addSongs(song)
                ListofAlbums.append(albomforlist)

            actor = Artist(name, surname, releaseYear, ListofAlbums, songList)
            ListofArtists.append(actor)


        platform = Platform()
        for arti in ListofArtists:
            platform.addArtists(arti)
        return platform

