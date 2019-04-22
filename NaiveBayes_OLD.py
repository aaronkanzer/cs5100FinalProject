from MovieCSVReader import Movie
from SummaryOfMovies import SummaryOfMovies

class NaiveBayes_OLD:

    def __init__(self):
        self.summaryOfMovies = SummaryOfMovies()
        self.castToRev = {}
        self.crewToRev = {}
        self.budgetToRev = {'0': [0,0,0,0,0], '1': [0,0,0,0,0], '2': [0,0,0,0,0], '3': [0,0,0,0,0], "4": [0,0,0,0,0]}
        self.genre = {}
        self.popularity = {}


    def getCastToRev(self):
        return self.castToRev

    def budgetToRev(self):
        return self.budgetToRev

    def getSummaryOfMovies(self):
        return self.summaryOfMovies

    # Creates and returns a dictionary of actors and a list of their revenue [0] and total movies [1]
    def featureCast(self):
        trainSet = self.summaryOfMovies.getTrainMovies()

        for i in range(len(trainSet)):
            cast = trainSet[i].getCast()

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

    # Creates and returns a dictionary of actors and a list of their revenue [0] and total movies [1]
    def featureCrew(self):
        trainSet = self.summaryOfMovies.getTrainMovies()

        for i in range(len(trainSet)):
            crew = trainSet[i].getCrew()

            for j in crew:
                if ('id' in j):
                    if (j['id'] in self.crewToRev and (j['job'] == "Director" or j['job'] == "Executive Producer" or j['job'] == "Producer" or j['job'] == 'Writer')):
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


    # def featureBudget(self):
    #     trainSet = self.summaryOfMovies.getTrainMovies()
    #
    #     for i in range(len(trainSet)):
    #         budget = int(trainSet[i].getBudget())
    #         rev = trainSet[i].getRevenueInterval()
    #
    #         if budget == 0:
    #             continue
    #         if (budget < 10000):
    #             self.addIntervalCounts('0', rev)
    #         elif(budget < 1000000):
    #             self.addIntervalCounts('1', rev)
    #         elif(budget < 5000000):
    #             self.addIntervalCounts('2', rev)
    #         elif(budget < 10000000):
    #             self.addIntervalCounts('3', rev)
    #         else:
    #             self.addIntervalCounts('4', rev)
    #
    # def addIntervalCounts(self, budget, rev):
    #     if (rev == .5):
    #         self.budgetToRev[budget][0] += 1
    #     elif (rev == 1):
    #         self.budgetToRev[budget][1] += 1
    #     elif (rev == 40):
    #         self.budgetToRev[budget][2] += 1
    #     elif (rev == 150):
    #         self.budgetToRev[budget][3] += 1
    #     elif (rev == 151):
    #         self.budgetToRev[budget][4] += 1


    # Takes a list of dictionaries of cast members
    def runTestData(self):
        # Train the model
        self.featureCast()
        self.featureCrew()
        # self.featureBudget()

        #Get test movies
        testMovies = self.summaryOfMovies.getTestMovies()
        totalTests = len(testMovies)
        correctPredictions = 0

        for movie in testMovies:
            totalProbability = [0, 0, 0, 0, 0]
            # Laplace smoothing by starting at 1
            castIntervalCounts = [1, 1, 1, 1, 1]
            crewIntervalCounts = [1, 1, 1, 1, 1]
            # obtain probabilities for P(interval | cast)
            for i in movie.getCast():
                if ('id' in i):
                    if (i['id'] in self.castToRev):
                        castIntervalCounts[0] += self.castToRev[i['id']][1]
                        castIntervalCounts[1] += self.castToRev[i['id']][2]
                        castIntervalCounts[2] += self.castToRev[i['id']][3]
                        castIntervalCounts[3] += self.castToRev[i['id']][4]
                        castIntervalCounts[4] += self.castToRev[i['id']][5]
            sum = castIntervalCounts[0] + castIntervalCounts[1] + castIntervalCounts[2] + castIntervalCounts[3] + castIntervalCounts[4]
            castProbability = [0, 0, 0, 0 , 0]
            castProbability[0] = castIntervalCounts[0] / float(sum)
            castProbability[1] = castIntervalCounts[1] / float(sum)
            castProbability[2] = castIntervalCounts[2] / float(sum)
            castProbability[3] = castIntervalCounts[3] / float(sum)
            castProbability[4] = castIntervalCounts[4] / float(sum)


            # Obtain probabilities for P(interval | crew)
            for i in movie.getCrew():
                if ('id' in i):
                    if (i['id'] in self.crewToRev):
                        crewIntervalCounts[0] += self.crewToRev[i['id']][1]
                        crewIntervalCounts[1] += self.crewToRev[i['id']][2]
                        crewIntervalCounts[2] += self.crewToRev[i['id']][3]
                        crewIntervalCounts[3] += self.crewToRev[i['id']][4]
                        crewIntervalCounts[4] += self.crewToRev[i['id']][5]
            sum = crewIntervalCounts[0] + crewIntervalCounts[1] + crewIntervalCounts[2] + crewIntervalCounts[3] + crewIntervalCounts[4]
            crewProbability = [0, 0, 0, 0 , 0]
            crewProbability[0] = crewIntervalCounts[0] / float(sum)
            crewProbability[1] = crewIntervalCounts[1] / float(sum)
            crewProbability[2] = crewIntervalCounts[2] / float(sum)
            crewProbability[3] = crewIntervalCounts[3] / float(sum)
            crewProbability[4] = crewIntervalCounts[4] / float(sum)


            # Obtain total probabilities
            totalProbability[0] = castProbability[0] * crewProbability[0]
            totalProbability[1] = castProbability[1] * crewProbability[1]
            totalProbability[2] = castProbability[2] * crewProbability[2]
            totalProbability[3] = castProbability[3] * crewProbability[3]
            totalProbability[4] = castProbability[4] * crewProbability[4]

            # sum0 = float(self.budgetToRev['0'][0] + self.budgetToRev['0'][1] + self.budgetToRev['0'][2] + self.budgetToRev['0'][3] + self.budgetToRev['0'][4])
            # sum1 = float(self.budgetToRev['1'][0] + self.budgetToRev['1'][1] + self.budgetToRev['1'][2] + self.budgetToRev['1'][3] + self.budgetToRev['1'][4])
            # sum2 = float(self.budgetToRev['2'][0] + self.budgetToRev['2'][1] + self.budgetToRev['2'][2] + self.budgetToRev['2'][3] + self.budgetToRev['2'][4])
            # sum3 = float(self.budgetToRev['3'][0] + self.budgetToRev['3'][1] + self.budgetToRev['3'][2] + self.budgetToRev['3'][3] + self.budgetToRev['3'][4])
            # sum4 = float(self.budgetToRev['4'][0] + self.budgetToRev['4'][1] + self.budgetToRev['4'][2] + self.budgetToRev['4'][3] + self.budgetToRev['4'][4])
            #
            # budget = movie.getBudget()
            # if (budget != 0):
            #     if (budget < 10000):
            #         totalProbability[0] = totalProbability[0] * (self.budgetToRev['0'][0] / sum0)
            #         totalProbability[1] = totalProbability[1] * (self.budgetToRev['0'][1] / sum0)
            #         totalProbability[2] = totalProbability[2] * (self.budgetToRev['0'][2] / sum0)
            #         totalProbability[3] = totalProbability[3] * (self.budgetToRev['0'][3] / sum0)
            #         totalProbability[4] = totalProbability[4] * (self.budgetToRev['0'][4] / sum0)
            #     elif(budget < 1000000):
            #         totalProbability[0] = totalProbability[0] * (self.budgetToRev['1'][0] / sum1)
            #         totalProbability[1] = totalProbability[1] * (self.budgetToRev['1'][1] / sum1)
            #         totalProbability[2] = totalProbability[2] * (self.budgetToRev['1'][2] / sum1)
            #         totalProbability[3] = totalProbability[3] * (self.budgetToRev['1'][3] / sum1)
            #         totalProbability[4] = totalProbability[4] * (self.budgetToRev['1'][4] / sum1)
            #     elif(budget < 5000000):
            #         totalProbability[0] = totalProbability[0] * (self.budgetToRev['2'][0] / sum2)
            #         totalProbability[1] = totalProbability[1] * (self.budgetToRev['2'][1] / sum2)
            #         totalProbability[2] = totalProbability[2] * (self.budgetToRev['2'][2] / sum2)
            #         totalProbability[3] = totalProbability[3] * (self.budgetToRev['2'][3] / sum2)
            #         totalProbability[4] = totalProbability[4] * (self.budgetToRev['2'][4] / sum2)
            #     elif(budget < 10000000):
            #         totalProbability[0] = totalProbability[0] * (self.budgetToRev['3'][0] / sum3)
            #         totalProbability[1] = totalProbability[1] * (self.budgetToRev['3'][1] / sum3)
            #         totalProbability[2] = totalProbability[2] * (self.budgetToRev['3'][2] / sum3)
            #         totalProbability[3] = totalProbability[3] * (self.budgetToRev['3'][3] / sum3)
            #         totalProbability[4] = totalProbability[4] * (self.budgetToRev['3'][4] / sum3)
            #     else:
            #         totalProbability[0] = totalProbability[0] * (self.budgetToRev['4'][0] / sum4)
            #         totalProbability[1] = totalProbability[1] * (self.budgetToRev['4'][1] / sum4)
            #         totalProbability[2] = totalProbability[2] * (self.budgetToRev['4'][2] / sum4)
            #         totalProbability[3] = totalProbability[3] * (self.budgetToRev['4'][3] / sum4)
            #         totalProbability[4] = totalProbability[4] * (self.budgetToRev['4'][4] / sum4)


            predictedRevProb = max(totalProbability)
            for prob in range(len(totalProbability)):
                if (totalProbability[prob] == predictedRevProb):
                    predictedInterval = prob

            actualRev = movie.getRevenueInterval()
            if (actualRev == .5 and predictedInterval == 0):
                correctPredictions += 1
            elif (actualRev == 1 and predictedInterval == 1):
                correctPredictions += 1
            elif (actualRev == 40 and predictedInterval == 2):
                correctPredictions += 1
            elif (actualRev == 150 and predictedInterval == 3):
                correctPredictions += 1
            elif (actualRev == 151 and predictedInterval == 4):
                correctPredictions += 1

        print (correctPredictions)
        print (totalTests)
        print(self.budgetToRev)


x = NaiveBayes_OLD()
x.runTestData()
