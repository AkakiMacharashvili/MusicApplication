
class Artist:
    def __init__(self, firstName, lastName, birthYear, albums, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__albums = albums
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName

    def getSecondName(self):
        return self.__lastName

    def getBirthYear(self):
        return self.__birthYear

    def getAlbums(self):
        return self.__albums

    def getSingle(self):
        return self.__singles

    def mostLikedSong(self):
        lst = []
        self.__singles.sort(key=(lambda x: x.getLikes()))
        lst.append(self.__singles[len(self.__singles) - 1])

        for album in self.__albums:
            album.sortByPopularity(False)
            lst.append(album.songList()[0])

        lst.sort(key=(lambda x: x.getLikes()))
        return lst[len(lst) - 1]

    def leastLikedSong(self):
        lst = []
        self.__singles.sort(key=(lambda x: x.getLikes()))
        lst.append(self.__singles[0])

        for album in self.__albums:
            album.sortByPopularity(True)
            lst.append(album.songList()[0])

        lst.sort(key=(lambda x: x.getLikes()))
        return lst[0]

    def totalLikes(self):
        total = 0
        for song in self.__singles:
            total += song.getLikes()
        for album in self.__albums:
            for song in album.getSongs():
                total += song.getLikes()
        return total

    def __str__(self):
        strg = 'Name:' + str(self.__firstName) + ' ' + str(self.__lastName) + ',Birth year:' + str(self.__birthYear)
        strg += ',Total likes:' + str(self.totalLikes())
        return strg


