import datetime
import time

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ut = time.time()
    dt_now = datetime.datetime.now()
    print("unix:%s, datetime:%s".format(ut, dt_now))

    year = [1980, 1985, 1990, 2000, 2010, 2018]
    weight = [3, 15, 25, 55, 62, 58]
    plt.plot(year, weight)
    plt.show()
