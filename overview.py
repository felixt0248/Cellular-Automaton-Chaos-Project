import numpy as np
from matplotlib import pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 25,
    "mathtext.fontset": "cm",
})

class Overview:
    def __init__(self, data):
        self.fish, self.shark = map(list, zip(*data))
        self.t = np.arange(0, len(self.fish), 1)

    def show(self, settings):
        if settings["show_plots"]:
            self.plot()
        if settings["print_results"]:
            self.print_results()

    def print_results(self):
        pass

    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.t, self.fish, label="Fish")
        ax.plot(self.t, self.shark, label="Sharks")
        ax.set_xlabel("Time")
        ax.set_ylabel("Population")
        ax.legend()
        plt.show()

        fig, ax = plt.subplots()
        ax.plot(self.fish, self.shark)
        ax.set_xlabel("Fish")
        ax.set_ylabel("Sharks")
        plt.show()
