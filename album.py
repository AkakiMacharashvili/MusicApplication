
class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def addSongs(self, *args):
        total = 0
        for song in args:
            add = True
            for sng in self.__songs:
                if song.getDuration() == sng.getDuration() and song.getReleaseYear() == sng.getReleaseYear():
                    if song.getTitle() == sng.getTitle():
                        add = False
            if add:
                self.__songs.append(song)
                total += 1
        return total

    def sortBy(self, byKey, reverse):
        return sorted(self.__songs, key=byKey, reverse=reverse)


    def songList(self):
        lst = []
        for song in self.__songs:
            lst.append(song)
        return lst

    def sortByReleaseYear(self, reverse):
        return Album.sortBy(self, (lambda x: x.getReleaseYear()), reverse)

    def sortByName(self, reverse):
        return Album.sortBy(self, (lambda x: x.getTitle()), reverse)

    def sortByPopularity(self, reverse):
        return Album.sortBy(self, (lambda x: x.getLikes()), reverse)

    def sortByDuration(self, reverse):
        return Album.sortBy(self, (lambda x: x.getDuration()), reverse)

    def __str__(self):
        strg = "Title:" + str(self.__title) + ",Release year:" + str(self.__releaseYear) + ",songs:{"
        for song in self.__songs:
            strg += str(song) + "|"
        if len(self.__songs) > 0:
            strg = strg[0:(len(strg) - 1)]
        return strg[0:(len(strg))] + "}"

