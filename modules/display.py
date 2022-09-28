import matplotlib.pyplot as plt

def myplot(minv, maxv, step, fun1, fun2):
    plt.ion()
    plt.xlabel('the x axis')
    plt.ylabel('the y axis')
    plt.plot()
    plt.legend(loc='upper right')
    plt.show()

myplot()