import numpy as np
import csv

class Calculations:
    def __init__(self, path):
        reader = csv.reader(open(path, "rb"), delimiter=",")
        x = list(reader)
        self.matrix = np.array(x).astype(np.float64)

    def mean_array(self):  # find mean values of columns
        self.cols = self.matrix.shape[1]
        self.rows = self.matrix.shape[0]

        mean_values = []

        for i in range(0, self.cols):
            mean_values.append(np.mean(self.matrix[:, i:i + 1]))

        return mean_values

    def get_final_values(self, mean_array):
        new_matrix = np.copy(self.matrix)  # new matrix after reduce mean values
        for x in range(0, self.cols):
            for y in range(0, self.rows):
                new_matrix[y][x] = (self.matrix[y][x] - mean_array[x]) * (self.matrix[y][x] - mean_array[x])

        final_values = []
        for i in range(0, self.cols):
            value = np.sum(new_matrix[:, i:i + 1])
            value = value / (self.rows - 1)
            value = np.sqrt(value)
            final_values.append(value)

        return final_values


#local minima class
class Local_Minima:
    def __init__(self, path):
        reader = csv.reader(open(path, "rb"), delimiter=",")
        x = list(reader)
        self.matrix = np.array(x).astype(np.float64)
        self.rows = self.matrix.shape[0]
        self.cols = self.matrix.shape[1]
        self.y = self.matrix[:, :1]
        self.x = self.matrix[:, 1:]

    def findLocalMinima(self):
        self.decreasing = True
        self.localMinima_x = []
        self.localMinima_y = []
        if (self.y[0] > self.y[1]):
            self.decreasing = True

        for i in range(0, self.rows - 2):
            if (self.y[i] > self.y[i + 1] and self.y[i + 1] < self.y[i + 2]):
                self.localMinima_x.append(self.x[i + 1])
                self.localMinima_y.append(self.y[i + 1])

        combine = np.column_stack((self.localMinima_x, self.localMinima_y)) #combine x and y coordinates
        return combine


##########################################################################################


cal = Calculations("labExercise01.csv")   #create object for find Sn values
print "Sn values : ", cal.get_final_values(cal.mean_array())

localm = Local_Minima("bonusExercise.csv")  #create object to fin local minima and find local minima
localMinima = localm.findLocalMinima()
print "Local minima (x,y) : ", localMinima
