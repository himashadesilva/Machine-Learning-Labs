import unittest

import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal

class Lab3 :
    def __init__(self,csvFile,cols):

        self.cols = cols
        self.colSize = len(cols)
        self.df = pd.read_csv(csvFile,names=['a','b','c','d','e'])
        self.df.shape
        self.df = self.df.fillna(0)


        #print self.df.corr()

    def covariance(self):
        #x_mean = self.df.get(x).isnull().mean()
        #y_mean = self.df.get(y).isnull().mean()

        covMatrix = np.zeros(shape=(self.colSize,self.colSize),dtype=float)

        for i in range(0,self.colSize):
            for j in range(0,self.colSize):
                if i == j:
                    cov = self.df.loc[:,self.cols[i]].var()
                else:
                    X = self.df.loc[:, self.cols[i]]
                    Y = self.df.loc[:, self.cols[j]]

                    x_mean = X.mean()
                    y_mean = Y.mean()

                    value = 0
                    for k in range(0,X.size):
                        xi = X[k]
                        yi = Y[k]
                        value = value + ((xi-x_mean) * (yi - y_mean))/(X.size-1)

                    cov = value

                covMatrix[i][j] = cov

        return pd.DataFrame(covMatrix,columns=self.cols,index=self.cols)


        #print x_mean

    def corelation(self):
        corMatrix = np.zeros(shape=(self.colSize,self.colSize),dtype=float)

        for i in range(0,self.colSize):
            for j in range(0,self.colSize):
                X = self.df.loc[:, self.cols[i]]
                Y = self.df.loc[:, self.cols[j]]

                sdx = X.std()
                sdy = Y.std()

                cov_value = 0;

                x_mean = X.mean()
                y_mean = Y.mean()

                value = 0
                for k in range(0, X.size):
                    xi = X[k]
                    yi = Y[k]
                    value = value + ((xi - x_mean) * (yi - y_mean)) / (X.size - 1)

                cov_value = value

                val = (cov_value/(sdx*sdy))

                corMatrix[i][j] = val

        return pd.DataFrame(corMatrix,columns=self.cols,index=self.cols)




class Test(unittest.TestCase):

    def setUp(self):
        print "set up"
        cols = ['a', 'b', 'c', 'd', 'e']
        self.lab3 = Lab3("lab03Exercise.csv", cols)



    def test_covariance(self):
        actual = self.lab3.covariance()
        correct = self.lab3.df.cov()

        assert_frame_equal(actual,correct)
        print "Actual cov :\n", actual , "\n Correct cov: \n", correct

    def test_correlation(self):
        actual = self.lab3.corelation()
        correct = self.lab3.df.corr()

        assert_frame_equal(actual, correct)
        print "Actual corr :\n", actual, "\n Correct corr: \n", correct

    def tearDown(self):
        print "tear down"

if __name__ == '__main__':
    unittest.main()
