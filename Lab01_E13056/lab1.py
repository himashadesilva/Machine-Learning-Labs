import numpy as np
import csv

class Calculations:
    def __init__(self,path):
        reader = csv.reader(open(path,"rb"),delimiter=",")
        x = list(reader)
        self.matrix = np.array(x).astype("float")

    def mean_array(self):
        self.cols = self.matrix.shape[1]
        self.rows = self.matrix.shape[0]

        mean_values = []

        for i in range(0,self.cols):
            mean_values.append(np.mean(self.matrix[:,i:i+1]))

        return mean_values

    def get_final_values(self,mean_array):
        new_matrix = np.copy(self.matrix)
        for x in range(0,self.cols):
            for y in range(0,self.rows):
                new_matrix[y][x] = (self.matrix[y][x] - mean_array[x])*(self.matrix[y][x] - mean_array[x])

        final_values = []
        for i in range(0,self.cols):
            value = np.sum(new_matrix[:,i:i+1])
            value = value/(self.rows-1)
            value = np.sqrt(value)
            final_values.append(value)


        return final_values



cal = Calculations("labExercise01.csv")
print cal.get_final_values(cal.mean_array())