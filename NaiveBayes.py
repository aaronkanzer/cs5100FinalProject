from MovieCSVReader import Movie
from SummaryOfMovies import SummaryOfMovies

class NaiveBayes:

    def __init__(self):
        self.summaryOfMovies = SummaryOfMovies()
        self.actorToRev = {}

    def getActorToRev(self):
        return self.actorToRev

    def getSummaryOfMovies(self):
        return self.summaryOfMovies

    # Creates and returns a dictionary of actors and a list of their revenue [0] and total movies [1]
    def featureCast(self):
        trainSet = self.summaryOfMovies.getTrainMovies()

        for i in range(len(trainSet)):
            cast = trainSet[i].getCast()

            for j in cast:
                if ('id' in j):
                    if (j['id'] in self.actorToRev):
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.actorToRev[j['id']][1] += 1
                        elif (rev == 1):
                            self.actorToRev[j['id']][2] += 1
                        elif (rev == 40):
                            self.actorToRev[j['id']][3] += 1
                        elif (rev == 150):
                            self.actorToRev[j['id']][4] += 1
                        elif (rev == 151):
                            self.actorToRev[j['id']][5] += 1
                    else:
                        self.actorToRev[j['id']] = [j['name'],0, 0, 0, 0, 0]
                        rev = trainSet[i].getRevenueInterval()
                        if (rev == .5):
                            self.actorToRev[j['id']][1] += 1
                        elif (rev == 1):
                            self.actorToRev[j['id']][2] += 1
                        elif (rev == 40):
                            self.actorToRev[j['id']][3] += 1
                        elif (rev == 150):
                            self.actorToRev[j['id']][4] += 1
                        elif (rev == 151):
                            self.actorToRev[j['id']][5] += 1

        # for key, value in actorToRev.iteritems():
        #     print(str(key) + ": \t\t\t\t" + '${:,.2f}'.format(float(value[0])/float(value[1])) + "\t\t\t\t" + str(value[1]))
        # print ("John Wayne: \t\t\t\t" + str(float(actorToRev['John Wayne'][0])/float(actorToRev['John Wayne'][1])) + "\t\t" + str(float(actorToRev['John Wayne'][1])))



    # Takes a list of dictionaries of cast members
    def model(self, cast):
        intervalCounts = [0, 0, 0, 0, 0]

        totalCount = 0

        for i in cast:
            if (i['id'] in self.actorToRev):
                intervalCounts[0] += self.actorToRev[i['id']][1]
                intervalCounts[1] += self.actorToRev[i['id']][2]
                intervalCounts[2] += self.actorToRev[i['id']][3]
                intervalCounts[3] += self.actorToRev[i['id']][4]
                intervalCounts[4] += self.actorToRev[i['id']][5]

        sum = intervalCounts[0] + intervalCounts[1] + intervalCounts[2] + intervalCounts[3] + intervalCounts[4]
        probability = [0, 0, 0, 0 , 0]
        probability[0] = intervalCounts[0] / float(sum)
        probability[1] = intervalCounts[1] / float(sum)
        probability[2] = intervalCounts[2] / float(sum)
        probability[3] = intervalCounts[3] / float(sum)
        probability[4] = intervalCounts[4] / float(sum)

        print (probability)
        print (intervalCounts)





x = NaiveBayes()
x.featureCast()
x.model(x.getSummaryOfMovies().getTestMovies()[4].getCast())
print (x.getSummaryOfMovies().getTestMovies()[4].getTitle())
