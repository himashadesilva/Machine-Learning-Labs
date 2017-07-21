import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import unittest

# my E no is E/13/056
# e1=0 , e2 = 5, e3 = 6

class  Gradient_Descent:

    def __init__(self,n,x,l,poly):
        self.n = n
        self.x = x
        self.l =l
        self.poly = poly


    def plot_fx(self):
        matplotlib.rc('xtick', labelsize=30)
        matplotlib.rc('ytick', labelsize=30)
        matplotlib.rc('axes', titlesize=30)
        matplotlib.rc('legend', fontsize=30)

        fig = plt.figure(figsize=(10, 10))
        fig.subplots_adjust(hspace=1)

        axes = plt.subplot(1, 1, 1)

        X = np.linspace(-2,6)
        Y = self.poly(X)
        axes.plot(X, Y, linewidth=1, ls='--', color='r', marker="*")
        plt.show()

    def local_minima(self):
        current_x = self.x
        previous_x = current_x
        grad = np.polyder(self.poly)
        previous_step_size = current_x
        while(previous_step_size>self.l):
            previous_x = current_x
            current_x = current_x - self.n*grad(current_x)
            previous_step_size = abs(current_x-previous_x)
            #print "sss"
        return current_x



class Test(unittest.TestCase):
    def setUp(self):
        lst = [0]*5

        lst[4] = 5   #polynomial f = 5
        poly = np.poly1d(lst)

        self.gda1 = Gradient_Descent(0.1,0,0.01,poly)  #initial x = 0

        lst[1] = 1
        lst[2] = -9
        lst[3] = 23
        lst[4] = -15
        poly = np.poly1d(lst)

        self.gda2 = Gradient_Descent(0.1, 2, 0.01, poly)  #intial x = 2

        self.gda3 = Gradient_Descent(0.1,0,0.01,poly)  #initial x = 0

        self.gda4 = Gradient_Descent(0.1, 5, 0.01, poly)  # initial x = 5

        self.gda5 = Gradient_Descent(0.4, 2, 0.01, poly)  # initial x = 2, learning rate = 0.4

    def test_local_m1(self):
        self.assertAlmostEqual(self.gda1.local_minima(),0)
        print "no local minima , function is y=5, print inital given x, this cant take as local minima"

    def test_local_m2(self):
        self.assertAlmostEqual(self.gda2.local_minima(),4.1512,3)
        print "has local minima near x = 4 and has local maxima near x = 1,initial x given as x = 2,\n therefore local minima gives correctly "
    def test_local_m3(self):
        self.assertAlmostEqual(self.gda3.local_minima(),0,3)
        print "has local minima near x = 4 and has local maxima near x = 1,initial x given as x = 0, therefore local minima is not correct "

    def test_local_m4(self):
        self.assertAlmostEqual(self.gda4.local_minima(),4.15,1)
        print "has local minima near x = 4 ,initial x given as x = 5, therefore local minima is correct "

    def test_local_m5(self): #chaning learning rate to 0.4
        self.assertAlmostEqual(self.gda5.local_minima(), 4.15, 1)
        print "for learning rate = 0.4 , it gives an answer for local minima, but after leaning rate 0.4, it gives an error"

    def tearDown(self):
        print "finshed test\n"

if __name__ == "__main__":

    lst = [0] * 5  # my function  fx = 5
    #lst[1] = 1
    #lst[2] = -9
    #lst[3] = 23
    lst[4] = 5
    poly = np.poly1d(lst)


    gda = Gradient_Descent(0.1,0,0.01,poly)   #n,x,lambda, plynomial
    gda.plot_fx() # for question 1, plot behavior of f(x)  (E/13/056 ---> f(x) = 5)
    print gda.local_minima()
    unittest.main()


    #Question 2 : we should give x near to local minima, if we give initial x before a local maxima (grad =0) , it will not go after
                # local maixa, so it will not give correct local minima


    #Questiion 3 : when increase learning rate we can get local minima value quickly,
    #              but if learning rate incrase more it will skipped the local minima


    #Question 4: my polynomial was f(x) = 5, therefore there is no local minima
                # it will give initial x that we give.