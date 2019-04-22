from MovieCSVReader import Movie
from SummaryOfMovies import SummaryOfMovies

class NaiveBayes:

    def __init__(self):
        # Get the data
        self.summaryOfMovies = SummaryOfMovies()

        # Variables used to calculate probabilities from training data
        self.castToRev = {}
        self.crewToRev = {}
        self.genres = {}
        self.prodComp = {}
        self.keywords = {}
        self.popularity = {}
        self.runTime = {}

        # Keeps track of the total Probability for a movie for each interval
        self.totalProbability = [1, 1, 1, 1, 1]
        self.intervalProbability = [0,0,0,0,0]

        # Values used to assess our model
        self.correctPredictions = 0
        self.totalPredictions = 0
        self.intervalCorrectPred = [0,0,0,0,0]

    def getCastToRev(self):
        return self.castToRev

    def budgetToRev(self):
        return self.budgetToRev

    def getSummaryOfMovies(self):
        return self.summaryOfMovies

    # Creates and returns a dictionary of actors and a list of their revenue [0] and total movies [1]
    def trainFeatureCast(self):
        trainSet = self.summaryOfMovies.getTrainMovies()

        for i in range(len(trainSet)):
            cast = trainSet[i].getCast

            for j in cast:
                if ('id' in j ):
                    if (j['id'] in self.castToRev):
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.castToRev[j['id']][1] += 1
                        elif (rev == 1):
                            self.castToRev[j['id']][2] += 1
                        elif (rev == 40):
                            self.castToRev[j['id']][3] += 1
                        elif (rev == 150):
                            self.castToRev[j['id']][4] += 1
                        elif (rev == 151):
                            self.castToRev[j['id']][5] += 1
                    else:
                        self.castToRev[j['id']] = [j['name'], 1, 1, 1, 1, 1]
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.castToRev[j['id']][1] += 1
                        elif (rev == 1):
                            self.castToRev[j['id']][2] += 1
                        elif (rev == 40):
                            self.castToRev[j['id']][3] += 1
                        elif (rev == 150):
                            self.castToRev[j['id']][4] += 1
                        elif (rev == 151):
                            self.castToRev[j['id']][5] += 1

    def trainFeatureCrew(self):
        trainSet = self.summaryOfMovies.getTrainMovies()

        for i in range(len(trainSet)):
            crew = trainSet[i].getCrew()

            for j in crew:
                if ('id' in j):
                    if (j['id'] in self.crewToRev and (j['job'] == "Director" or j['job'] == "Producer" or j['job'] == 'Writer')):
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.crewToRev[j['id']][1] += 1
                        elif (rev == 1):
                            self.crewToRev[j['id']][2] += 1
                        elif (rev == 40):
                            self.crewToRev[j['id']][3] += 1
                        elif (rev == 150):
                            self.crewToRev[j['id']][4] += 1
                        elif (rev == 151):
                            self.crewToRev[j['id']][5] += 1
                    else:
                        self.crewToRev[j['id']] = [j['name'], 1, 1, 1, 1, 1]
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.crewToRev[j['id']][1] += 1
                        elif (rev == 1):
                            self.crewToRev[j['id']][2] += 1
                        elif (rev == 40):
                            self.crewToRev[j['id']][3] += 1
                        elif (rev == 150):
                            self.crewToRev[j['id']][4] += 1
                        elif (rev == 151):
                            self.crewToRev[j['id']][5] += 1


    def trainFeatureGenre(self):
        trainSet = self.summaryOfMovies.getTrainMovies()

        for i in range(len(trainSet)):
            genres = trainSet[i].getGenres()

            for j in genres:
                if ('id' in j):
                    if (j['id'] in self.genres):
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.genres[j['id']][1] += 1
                        elif (rev == 1):
                            self.genres[j['id']][2] += 1
                        elif (rev == 40):
                            self.genres[j['id']][3] += 1
                        elif (rev == 150):
                            self.genres[j['id']][4] += 1
                        elif (rev == 151):
                            self.genres[j['id']][5] += 1
                    else:
                        self.genres[j['id']] = [j['name'], 1, 1, 1, 1, 1]
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.genres[j['id']][1] += 1
                        elif (rev == 1):
                            self.genres[j['id']][2] += 1
                        elif (rev == 40):
                            self.genres[j['id']][3] += 1
                        elif (rev == 150):
                            self.genres[j['id']][4] += 1
                        elif (rev == 151):
                            self.genres[j['id']][5] += 1




    def trainFeatureProductionCompany(self):
        trainSet = self.summaryOfMovies.getTrainMovies()
        i = 0
        for i in range(len(trainSet)):
            prodComp = trainSet[i].getProdComp()

            for j in prodComp:
                if ('id' in j):
                    if (j['id'] in self.prodComp):
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.prodComp[j['id']][1] += 1
                        elif (rev == 1):
                            self.prodComp[j['id']][2] += 1
                        elif (rev == 40):
                            self.prodComp[j['id']][3] += 1
                        elif (rev == 150):
                            self.prodComp[j['id']][4] += 1
                        elif (rev == 151):
                            self.prodComp[j['id']][5] += 1
                    else:
                        self.prodComp[j['id']] = [j['name'], 1, 1, 1, 1, 1]
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.prodComp[j['id']][1] += 1
                        elif (rev == 1):
                            self.prodComp[j['id']][2] += 1
                        elif (rev == 40):
                            self.prodComp[j['id']][3] += 1
                        elif (rev == 150):
                            self.prodComp[j['id']][4] += 1
                        elif (rev == 151):
                            self.prodComp[j['id']][5] += 1


    def trainFeatureKeywords(self):
        trainSet = self.summaryOfMovies.getTrainMovies()
        i = 0
        for i in range(len(trainSet)):
            keywords = trainSet[i].getKeyWords()

            for j in keywords:
                if ('id' in j):
                    if (j['id'] in self.keywords):
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.keywords[j['id']][1] += 1
                        elif (rev == 1):
                            self.keywords[j['id']][2] += 1
                        elif (rev == 40):
                            self.keywords[j['id']][3] += 1
                        elif (rev == 150):
                            self.keywords[j['id']][4] += 1
                        elif (rev == 151):
                            self.keywords[j['id']][5] += 1
                    else:
                        self.keywords[j['id']] = [j['name'], 1, 1, 1, 1, 1]
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.keywords[j['id']][1] += 1
                        elif (rev == 1):
                            self.keywords[j['id']][2] += 1
                        elif (rev == 40):
                            self.keywords[j['id']][3] += 1
                        elif (rev == 150):
                            self.keywords[j['id']][4] += 1
                        elif (rev == 151):
                            self.keywords[j['id']][5] += 1


    def trainFeaturePopularity(self):
        trainSet = self.summaryOfMovies.getTrainMovies()
        i = 0
        for i in range(len(trainSet)):
            popularity = trainSet[i].getPopularity()
            if (popularity in self.popularity):
                rev = trainSet[i].getRevenueInterval()
                if (rev == .5):
                    self.popularity[popularity][1] += 1
                elif (rev == 1):
                    self.popularity[popularity][2] += 1
                elif (rev == 40):
                    self.popularity[popularity][3] += 1
                elif (rev == 150):
                    self.popularity[popularity][4] += 1
                elif (rev == 151):
                    self.popularity[popularity][5] += 1
            else:
                self.popularity[popularity] = [popularity, 1, 1, 1, 1, 1]
                rev = trainSet[i].getRevenueInterval()
                if (rev == .5):
                    self.popularity[popularity][1] += 1
                elif (rev == 1):
                    self.popularity[popularity][2] += 1
                elif (rev == 40):
                    self.popularity[popularity][3] += 1
                elif (rev == 150):
                    self.popularity[popularity][4] += 1
                elif (rev == 151):
                    self.popularity[popularity][5] += 1


    def trainFeatureRunTime(self):
        trainSet = self.summaryOfMovies.getTrainMovies()
        i = 0
        for i in range(len(trainSet)):
            runTime = trainSet[i].getRuntime()
            if (runTime != ''):
                if (runTime in self.runTime):
                    rev = trainSet[i].getRevenueInterval()
                    if (rev == .5):
                        self.runTime[runTime][1] += 1
                    elif (rev == 1):
                        self.runTime[runTime][2] += 1
                    elif (rev == 40):
                        self.runTime[runTime][3] += 1
                    elif (rev == 150):
                        self.runTime[runTime][4] += 1
                    elif (rev == 151):
                        self.runTime[runTime][5] += 1
                else:
                    self.runTime[runTime] = [runTime, 1, 1, 1, 1, 1]
                    rev = trainSet[i].getRevenueInterval()
                    if (rev == .5):
                        self.runTime[runTime][1] += 1
                    elif (rev == 1):
                        self.runTime[runTime][2] += 1
                    elif (rev == 40):
                        self.runTime[runTime][3] += 1
                    elif (rev == 150):
                        self.runTime[runTime][4] += 1
                    elif (rev == 151):
                        self.runTime[runTime][5] += 1



    def testCast(self, movie):
        # Obtain probabilities for P(interval | cast)
        for i in movie.getCast():
            if ('id' in i):
                if (i['id'] in self.castToRev):
                    sum = self.castToRev[i['id']][1] + self.castToRev[i['id']][2] + self.castToRev[i['id']][3] + self.castToRev[i['id']][4] + self.castToRev[i['id']][5]
                    self.totalProbability[0] = self.totalProbability[0] * (self.castToRev[i['id']][1] / float(sum))
                    self.totalProbability[1] = self.totalProbability[1] * (self.castToRev[i['id']][2] / float(sum))
                    self.totalProbability[2] = self.totalProbability[2] * (self.castToRev[i['id']][3] / float(sum))
                    self.totalProbability[3] = self.totalProbability[3] * (self.castToRev[i['id']][4] / float(sum))
                    self.totalProbability[4] = self.totalProbability[4] * (self.castToRev[i['id']][5] / float(sum))

    def testCrew(self, movie):
        # Obtain probabilities for P(interval | crew)
        for i in movie.getCrew():
            if ('id' in i):
                if (i['id'] in self.crewToRev):
                    sum = self.crewToRev[i['id']][1] + self.crewToRev[i['id']][2] + self.crewToRev[i['id']][3] + self.crewToRev[i['id']][4] + self.crewToRev[i['id']][5]
                    self.totalProbability[0] = self.totalProbability[0] * (self.crewToRev[i['id']][1] / float(sum))
                    self.totalProbability[1] = self.totalProbability[1] * (self.crewToRev[i['id']][2] / float(sum))
                    self.totalProbability[2] = self.totalProbability[2] * (self.crewToRev[i['id']][3] / float(sum))
                    self.totalProbability[3] = self.totalProbability[3] * (self.crewToRev[i['id']][4] / float(sum))
                    self.totalProbability[4] = self.totalProbability[4] * (self.crewToRev[i['id']][5] / float(sum))


    def testGenres(self, movie):
        # Obtain probabilities for P(interval | crew)
        for i in movie.getGenres():
            if ('id' in i):
                if (i['id'] in self.genres):
                    sum = self.genres[i['id']][1] + self.genres[i['id']][2] + self.genres[i['id']][3] + self.genres[i['id']][4] + self.genres[i['id']][5]
                    self.totalProbability[0] = self.totalProbability[0] * (self.genres[i['id']][1] / float(sum))
                    self.totalProbability[1] = self.totalProbability[1] * (self.genres[i['id']][2] / float(sum))
                    self.totalProbability[2] = self.totalProbability[2] * (self.genres[i['id']][3] / float(sum))
                    self.totalProbability[3] = self.totalProbability[3] * (self.genres[i['id']][4] / float(sum))
                    self.totalProbability[4] = self.totalProbability[4] * (self.genres[i['id']][5] / float(sum))

    def testProductionComapny(self, movie):
        # Obtain probabilities for P(interval | crew)
        for i in movie.getProdComp():
            if ('id' in i):
                if (i['id'] in self.prodComp):
                    sum = self.prodComp[i['id']][1] + self.prodComp[i['id']][2] + self.prodComp[i['id']][3] + self.prodComp[i['id']][4] + self.prodComp[i['id']][5]
                    self.totalProbability[0] = self.totalProbability[0] * (self.prodComp[i['id']][1] / float(sum))
                    self.totalProbability[1] = self.totalProbability[1] * (self.prodComp[i['id']][2] / float(sum))
                    self.totalProbability[2] = self.totalProbability[2] * (self.prodComp[i['id']][3] / float(sum))
                    self.totalProbability[3] = self.totalProbability[3] * (self.prodComp[i['id']][4] / float(sum))
                    self.totalProbability[4] = self.totalProbability[4] * (self.prodComp[i['id']][5] / float(sum))

    def testKeywords(self, movie):
        # Obtain probabilities for P(interval | crew)
        for i in movie.getKeyWords():
            if ('id' in i):
                if (i['id'] in self.keywords):
                    sum = self.keywords[i['id']][1] + self.keywords[i['id']][2] + self.keywords[i['id']][3] + self.keywords[i['id']][4] + self.keywords[i['id']][5]
                    self.totalProbability[0] = self.totalProbability[0] * (self.keywords[i['id']][1] / float(sum))
                    self.totalProbability[1] = self.totalProbability[1] * (self.keywords[i['id']][2] / float(sum))
                    self.totalProbability[2] = self.totalProbability[2] * (self.keywords[i['id']][3] / float(sum))
                    self.totalProbability[3] = self.totalProbability[3] * (self.keywords[i['id']][4] / float(sum))
                    self.totalProbability[4] = self.totalProbability[4] * (self.keywords[i['id']][5] / float(sum))

    def testPopularity(self, movie):
        # Obtain probabilities for P(interval | crew)
        popularity = movie.getPopularity()
        if (popularity in self.popularity):
            sum = self.popularity[popularity][1] + self.popularity[popularity][2] + self.popularity[popularity][3] + self.popularity[popularity][4] + self.popularity[popularity][5]
            self.totalProbability[0] = self.totalProbability[0] * (self.popularity[popularity][1] / float(sum))
            self.totalProbability[1] = self.totalProbability[1] * (self.popularity[popularity][2] / float(sum))
            self.totalProbability[2] = self.totalProbability[2] * (self.popularity[popularity][3] / float(sum))
            self.totalProbability[3] = self.totalProbability[3] * (self.popularity[popularity][4] / float(sum))
            self.totalProbability[4] = self.totalProbability[4] * (self.popularity[popularity][5] / float(sum))


    def testRunTime(self, movie):
        # Obtain probabilities for P(interval | crew)
        runTime = movie.getRuntime()
        if (runTime in self.runTime):
            sum = self.runTime[runTime][1] + self.runTime[runTime][2] + self.runTime[runTime][3] + self.runTime[runTime][4] + self.runTime[runTime][5]
            self.totalProbability[0] = self.totalProbability[0] * (self.runTime[runTime][1] / float(sum))
            self.totalProbability[1] = self.totalProbability[1] * (self.runTime[runTime][2] / float(sum))
            self.totalProbability[2] = self.totalProbability[2] * (self.runTime[runTime][3] / float(sum))
            self.totalProbability[3] = self.totalProbability[3] * (self.runTime[runTime][4] / float(sum))
            self.totalProbability[4] = self.totalProbability[4] * (self.runTime[runTime][5] / float(sum))

    def makePrediction(self, movie):
        self.totalPredictions += 1
        predictedRevProb = max(self.totalProbability)

        for prob in range(len(self.totalProbability)):
            if (self.totalProbability[prob] == predictedRevProb):
                predictedInterval = prob

        actualRev = movie.getRevenueInterval()
        if (actualRev == .5 and predictedInterval == 0):
            self.correctPredictions += 1
            self.intervalCorrectPred[0] += 1
        elif (actualRev == 1 and predictedInterval == 1):
            self.correctPredictions += 1
            self.intervalCorrectPred[1] += 1
        elif (actualRev == 40 and predictedInterval == 2):
            self.correctPredictions += 1
            self.intervalCorrectPred[2] += 1
        elif (actualRev == 150 and predictedInterval == 3):
            self.correctPredictions += 1
            self.intervalCorrectPred[3] += 1
        elif (actualRev == 151 and predictedInterval == 4):
            self.correctPredictions += 1
            self.intervalCorrectPred[4] += 1


    # Takes a list of dictionaries of cast members
    def runTestData(self):
        # Train the model
        self.trainFeatureCast()
        self.trainFeatureCrew()
        self.trainFeatureGenre()
        self.trainFeatureProductionCompany()
        self.trainFeatureKeywords()
        self.trainFeaturePopularity()
        self.trainFeatureRunTime()

        # Get test movies
        testMovies = self.summaryOfMovies.getTestMovies()
        totalTests = len(testMovies)
        correctPredictions = 0

        for movie in testMovies:
            self.totalProbability = [1, 1, 1, 1, 1]
            # Obtain probabilities for P(interval | cast)
            self.testCast(movie)
            self.testCrew(movie)
            self.testGenres(movie)
            self.testProductionComapny(movie)
            self.testKeywords(movie)
            self.testPopularity(movie)
            self.testRunTime(movie)
            self.makePrediction(movie)


        testIntervals = self.summaryOfMovies.getTestIntervals()





        print ("\nNaive Bayes\nCorrect Predictions: {}".format(self.correctPredictions))
        print ("Total Movies Tested: {}".format(self.totalPredictions))
        print ("Percentage Correct {:.2f}%".format((self.correctPredictions / float(self.totalPredictions) * 100)))




x = NaiveBayes()
x.runTestData()
