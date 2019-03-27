import csv
from MovieCSVReader import Movie

class SummaryOfMovies:

    def __init__(self):
        self.allMovies = []
        self.trainMovies = []
        self.testMovies = []

        # Setting up a dictionary of our intervals of revenue. Each key holds a list of movies
        self.trainIntervals = {}
        self.trainIntervals['.5M'] = []
        self.trainIntervals['1M'] = []
        self.trainIntervals['40M'] = []
        self.trainIntervals['150M'] = []
        self.trainIntervals['151M+'] = []

        self.testIntervals = {}
        self.testIntervals['.5M'] = []
        self.testIntervals['1M'] = []
        self.testIntervals['40M'] = []
        self.testIntervals['150M'] = []
        self.testIntervals['151M+'] = []


        with open('train.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    if (row[20][0] == "["):
                        cast = eval(row[20])
                    else:
                        cast = [{}]
                    newMovie = Movie(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                    row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],cast,row[21],row[22])
                    #print("Training Movie added: " + newMovie.getTitle())
                    #print (newMovie.getCast())
                    self.allMovies.append(newMovie)
                else:
                    line_count += 1

        self.splitData()
        self.countTrainSet()
        self.countTestSet()
        self.printTrainCount()
        self.printTestCount()

    def getTrainMovies(self):
        return self.trainMovies

    def getTestMovies(self):
        return self.testMovies

    def getAllMovies(self):
        return self.allMovies

    def getTrainIntervals(self):
        return self.trainIntervals

    # Splits the 3000 movies into 2 groups, a training set (2000 movies) and a testing set (1000) movies
    def splitData(self):
        trainSize = len(self.allMovies) * (2.0/3.0)
        testSize = len(self.allMovies) * (2.0/3.0)

        for i in range(len(self.allMovies)):
            if i < trainSize:
                self.trainMovies.append(self.allMovies[i])
            else:
                self.testMovies.append(self.allMovies[i])
        print('Split ' + str(len(self.allMovies)) + ' rows into train set with ' + str(len(self.trainMovies)) + ' movies and test set with ' + str(len(self.testMovies)) + ' movies')

    # Adds each movie in the training set into a particular list in the trainIntervals dictionarybased on the movies revenue
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

    # Prints the count each of our intervals for the training set
    def printTestCount(self):
        print("Processed " + str(len(self.testMovies)) + " movies for testing set")
        print ("0 - 500K: %d" % len(self.testIntervals['.5M']))
        print ("500K - 1M: %d" % len(self.testIntervals['1M']))
        print ("1M - 40M: %d" % len(self.testIntervals['40M']))
        print ("40M - 150M: %d" % len(self.testIntervals['150M']))
        print ("150M+: %d" % len(self.testIntervals['151M+']))
