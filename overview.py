import numpy as np
from matplotlib import pyplot as plt

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
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.plot(self.t, self.fish, label="Fish")
        ax1.plot(self.t, self.shark, label="Sharks")
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Population")
        ax1.set_title("Time Evolution of Populations")
        ax1.legend()

        ax2.plot(self.fish, self.shark)
        ax2.set_xlabel("Fish")
        ax2.set_ylabel("Sharks")
        ax2.set_title("Phase Diagram")

        plt.show()
