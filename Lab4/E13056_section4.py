from sklearn import datasets
from  sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class Scikit_learn :

    def printIris(self):   #question 2

        iris = datasets.load_iris()
        print iris


    def petal_width_toX(self):  # question 3
        iris = datasets.load_iris()
        X = iris.data[ : , 2:3]
        return X

    def classValuesToY(self):
        iris = datasets.load_iris()
        Y = []
        for index in range(len(iris.target)): #question 4
            if iris.target[index]==2:
                Y.append(1)
            else:
                Y.append(0)
        return Y

    def logistic_regression_model(self,X,Y): #question 5

        X_train, X_val, Y_train, Y_val = train_test_split(X , Y, test_size=0.2)
        log_reg = LogisticRegression()
        log_reg.fit(X_train,Y_train)
        y_proba = log_reg.predict(X_val)

        return y_proba

    def linear_regression_model(self,X,Y): #question 6

        X_train, X_val, Y_train, Y_val = train_test_split(X , Y, test_size=0.2)
        lin_reg = LinearRegression()
        lin_reg.fit(X_train,Y_train)
        return lin_reg.predict(X_val)


scikit = Scikit_learn()

scikit.printIris()

X = scikit.petal_width_toX()
Y = scikit.classValuesToY()

y_proba = scikit.logistic_regression_model(X,Y)

lin_reg = scikit.linear_regression_model(X,Y)

print "Logistic regression : ", y_proba
print "Lineear regression : ", lin_reg

