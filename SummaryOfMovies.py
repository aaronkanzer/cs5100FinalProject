import csv
from MovieCSVReader import Movie


# Reads in Movies and summarizes some data. Add more functions as needed
class SummaryOfMovies:

    def __init__(self):
        # Holds the list of all 3000 movies
        self.allMovies = []
        # Holds the list of movies in the training set
        self.trainMovies = []
        # Holds the list of movies in the testing set
        self.testMovies = []

        # Setting up a dictionary of our intervals of revenue for the train set. Each key holds a list of movies
        self.trainIntervals = {}
        self.trainIntervals['.5M'] = []
        self.trainIntervals['1M'] = []
        self.trainIntervals['40M'] = []
        self.trainIntervals['150M'] = []
        self.trainIntervals['151M+'] = []

        # Setting up a dictionary of our intervals of revenue for the test set. Each key holds a list of movies
        self.testIntervals = {}
        self.testIntervals['.5M'] = []
        self.testIntervals['1M'] = []
        self.testIntervals['40M'] = []
        self.testIntervals['150M'] = []
        self.testIntervals['151M+'] = []

        # Process all movies and add them to self.allMovies
        # Everything is loaded as a string. Use eval(row[x]) to create a list of dictionaries from a string.
        with open('train.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    # Creates a list of dictionaries from the string in the 'cast' row
                    if (row[20][0] == "["):
                        cast = eval(row[20])
                    else:
                        cast = [{}]
                    # Creates a list of dictionaries from the string in the 'crew' row
                    if (row[21] is not '' and row[21][0] == "["):
                        crew = eval(row[21])
                    else:
                        crew = [{}]
                    if (row[3] is not '' and row[3][0] == "["):
                        genres = eval(row[3])
                    else:
                        genres = [{}]
                    if (row[11] is not '' and row[11][0] == "["):
                        prodComps = eval(row[11])
                    else:
                        prodComps = [{}]
                    if (row[19] is not '' and row[19][0] == "["):
                        keywords = eval(row[19])
                    else:
                        keywords = [{}]
                    newMovie = Movie(row[0],row[1],row[2],genres,row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                    prodComps,row[12],row[13],row[14],row[15],row[16],row[17],row[18],keywords,cast,crew,row[22])
                    #print("Training Movie added: " + newMovie.getTitle())
                    #print (newMovie.getCast())
                    self.allMovies.append(newMovie)
                else:
                    line_count += 1

        # Split list of movies into a train and test set
        self.splitData()
        # Adds Movies in the train set into different interval bukcets
        self.countTrainSet()
        # Adds Movies in the test set into different interval bukcets
        self.countTestSet()
        # Prints the length of each list in trainIntervals
        # self.printTrainCount()
        # # Prints the length of each list in testIntervals
        # self.printTestCount()

    # Returns all 3000 Movies
    def getTrainMovies(self):
        return self.trainMovies

    # Returns a list of Movies from the training set
    def getTestMovies(self):
        return self.testMovies

    # Returns a list of Movies from the test set
    def getAllMovies(self):
        return self.allMovies

    # Returns a dictionary of train intervals with a list of movies for each interval
    def getTrainIntervals(self):
        return self.trainIntervals

    # Returns a dictionary of test intervals with a list of movies for each interval
    def getTestIntervals(self):
        return self.testIntervals

    # Splits the 3000 movies into 2 groups, a training set (2000 movies) and a testing set (1000) movies
    def splitData(self):
        trainSize = len(self.allMovies) * (2.0/3.0)
        testSize = len(self.allMovies) * (1.0/3.0)

        for i in range(len(self.allMovies)):
            if i < trainSize:
                self.trainMovies.append(self.allMovies[i])
            else:
                self.testMovies.append(self.allMovies[i])
        # print('Split ' + str(len(self.allMovies)) + ' rows into train set with ' + str(len(self.trainMovies)) + ' movies and test set with ' + str(len(self.testMovies)) + ' movies')

    # Adds each movie in the training set into a particular list in the trainIntervals dictionary based on the movies revenue
    def countTrainSet(self):
        for i in range(len(self.trainMovies)):
            if (self.trainMovies[i].getRevenueInterval() == .5):
                self.trainIntervals['.5M'].append(self.trainMovies[i])

            elif (self.trainMovies[i].getRevenueInterval() == 1):
                self.trainIntervals['1M'].append(self.trainMovies[i])

            elif (self.trainMovies[i].getRevenueInterval() == 40):
                self.trainIntervals['40M'].append(self.trainMovies[i])

            elif (self.trainMovies[i].getRevenueInterval() == 150):
                self.trainIntervals['150M'].append(self.trainMovies[i])

            else:
                self.trainIntervals['151M+'].append(self.trainMovies[i])

    # Adds each movie in the testing set into a particular list in the testIntervals dictionary based on the movies revenue
    def countTestSet(self):
        for i in range(len(self.testMovies)):
            if (self.testMovies[i].getRevenueInterval() == .5):
                self.testIntervals['.5M'].append(self.testMovies[i])

            elif (self.testMovies[i].getRevenueInterval() == 1):
                self.testIntervals['1M'].append(self.testMovies[i])

            elif (self.testMovies[i].getRevenueInterval() == 40):
                self.testIntervals['40M'].append(self.testMovies[i])

            elif (self.testMovies[i].getRevenueInterval() == 150):
                self.testIntervals['150M'].append(self.testMovies[i])

            else:
                self.testIntervals['151M+'].append(self.testMovies[i])

    # Prints the count each of our intervals for the training set
    def printTrainCount(self):
        print("Processed " + str(len(self.trainMovies)) + " movies for training set")
        print ("0 - 500K: %d" % len(self.trainIntervals['.5M']))
        print ("500K - 1M: %d" % len(self.trainIntervals['1M']))
        print ("1M - 40M: %d" % len(self.trainIntervals['40M']))
        print ("40M - 150M: %d" % len(self.trainIntervals['150M']))
        print ("150M+: %d" % len(self.trainIntervals['151M+']))

    # Prints the count each of our intervals for the testing set
    def printTestCount(self):
        print("Processed " + str(len(self.testMovies)) + " movies for testing set")
        print ("0 - 500K: %d" % len(self.testIntervals['.5M']))
        print ("500K - 1M: %d" % len(self.testIntervals['1M']))
        print ("1M - 40M: %d" % len(self.testIntervals['40M']))
        print ("40M - 150M: %d" % len(self.testIntervals['150M']))
        print ("150M+: %d" % len(self.testIntervals['151M+']))
