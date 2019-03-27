from MovieCSVReader import Movie
from SummaryOfMovies import SummaryOfMovies

class NaiveBayes:

    def __init__(self):
        self.summaryOfMovies = SummaryOfMovies()


    def featureCast(self):
        trainSet = self.summaryOfMovies.getTrainMovies()

        actorToRev  = {}

        cast = trainSet[0].getCast()
        print (cast[5])



x = NaiveBayes()
x.featureCast()
