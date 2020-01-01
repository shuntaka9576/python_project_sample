import datetime
import time
import typing

import matplotlib.pyplot as plt


class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age


if __name__ == "__main__":
    ut = time.time()
    dt_now = datetime.datetime.now()
    # print("unix:%s, datetime:%s".format(ut, dt_now))

    year: typing.List[int] = []
    year = [1980, 1985, 1990, 2000, 2010, 2018]

    weight = [3, 15, 25, 55, 62, 58]
    plt.plot(year, weight)
    plt.show()

    # year.append("aaa")
    persons = Person("takahahsi", 14)
    # persons = Person(13, "takahahsi")
