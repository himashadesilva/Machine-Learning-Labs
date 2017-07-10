import numpy as np
import csv

class Local_Minima:
    def __init__(self,path):
        reader = csv.reader(open(path, "rb"), delimiter=",")
        x = list(reader)
        self.matrix = np.array(x).astype("float")
        self.rows = self.matrix.shape[0]
        self.cols = self.matrix.shape[1]
#self.matrix[: , :1]
#self.matrix[: , 1:]

    def findLocalMinima(self):
        self.decreasing = True

        if(self.matrix[0:1 , :1]>self.matrix[1:2 , :1]):
            self.decreasing = True

localm = Local_Minima("bonusExercise.csv")

