import csv


class Movie:

    # Create new Movie object
    def __init__(self, id, collection, budget, genres, homepage, imdb_id, original_language, original_title,
    overview, popularity, poster_path, production_companies, production_countries, release_date, movieRuntime,
    spoken_languages, status, tagline, title, Keywords, cast, crew, revenue):
        # ******* Unsure if we need all of these categories -- some data probably doesn't matter to our models *********
        self.budget = budget
        self.genres = genres
        self.popularity = popularity
        self.production_companies = production_companies
        self.production_countries = production_countries
        self.release_date = release_date
        self.movieRuntime = movieRuntime
        self.spoken_languages = spoken_languages
        self.Keywords = Keywords
        self.cast = cast
        self.crew = crew
        self.revenue = revenue
        self.title = title

    # Returns integer
    def getBudget(self):
        return self.budget

    # Returns dictionary / list of potential genres that the movie could be
    def getGenres(self):
        return self.genres

    # Returns float -- unsure what numbers equate to
    def getPopularity(self):
        return int(float(self.popularity))

    # Returns dictionary / list of companies
    def getProdComp(self):
        return self.production_companies

    # Returns dictionary / list of countries associated with Movie
    def getProdCountries(self):
        return self.production_countries

    # Returns date??
    def getReleaseDate(self):
        return self.release_date

    # Returns integer (number of minutes)
    def getRuntime(self):
        if (self.movieRuntime != ''):
            return int(self.movieRuntime)
        else:
            return ''
        


    # Returns dictionary / list of languages that the movie is in
    def getLanguages(self):
        return self.spoken_languages

    # Returns dictionary / list of words that could be associated with movie
    def getKeyWords(self):
        return self.Keywords

    # Returns dictionary / list of actors / actresses in the movie
    def getCast(self):
        return self.cast

    # Returns dictionary / list of directors, producers, editors, etc.
    def getCrew(self):
        return self.crew

    # Returns the amount of $ generated at the box office
    def getRevenue(self):
        return int(self.revenue)

    # Returns name of movie
    def getTitle(self):
        return self.title

    # Returns a float value to determine how financially successful the movie was
    def getProfitRatio(self):
        return (self.revenue / self.budget)

    # Returns the upper limit of the interval of revenue that this movie falls into. If greater than 150 mil, it returns 151
    def getRevenueInterval(self):
        revenueAsInt = int(self.revenue)
        if (revenueAsInt <= 500000):
            return .5
        elif (revenueAsInt > 500000 and revenueAsInt <= 1000000):
            return 1
        elif (revenueAsInt > 1000000 and revenueAsInt <= 40000000):
            return 40
        elif (revenueAsInt > 40000000 and revenueAsInt <= 150000000):
            return 150
        elif (revenueAsInt > 150000000):
            return 151

trainMovies = []
testMovies = []

# # Process training data ---- make sure to change file path to work appropriately on local machine
# with open('train.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count > 0:
#             if (row[20][0] == "["):
#                 cast = eval(row[20])
#             else:
#                 cast = [{}]
#             newMovie = Movie(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
#             row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],cast,row[21],row[22])
#             #print("Training Movie added: " + newMovie.getTitle())
#             trainMovies.append(newMovie)
#         else:
#             line_count += 1
#     print("Processed " + str(len(trainMovies)) + " movies for training set")
#
#
#
# # Process test data ---- make sure to change file path to work appropriately on local machine
# with open('test.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if (row[20][0] == "["):
#             cast = eval(row[20])
#         else:
#             cast = [{}]
#         if line_count > 0:
#             newMovie = Movie(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
#             row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],0)
#             #print("Testing Movie added: " + newMovie.getTitle())
#             testMovies.append(testMovies)
#         else:
#             line_count += 1
#     print("Processed " + str(len(testMovies)) + " movies for testing set")
