import numpy as np
from matplotlib import pyplot as plt

class Overview:
    GRAPH_CUTOFF_FRACTION = 0.001

    def __init__(self, data):
        self.fish, self.shark = map(list, zip(*data))
        self.t = np.arange(0, len(self.fish), 1)

    def show(self, settings):
        if settings["show_plots"]:
            self.plot()
        if settings["print_results"]:
            self.print_results()

    def print_results(self):
        print("fish standard deviation: ", np.std(self.fish))
        print("shark standard deviation: ", np.std(self.shark))

    def get_power_spectrum(self):
        fish_deviation = self.fish - np.mean(self.fish)
        shark_deviation = self.shark - np.mean(self.shark)
        fish_power = np.abs(np.fft.rfft(fish_deviation))**2
        shark_power = np.abs(np.fft.rfft(shark_deviation))**2
        freqs = np.fft.rfftfreq(len(self.fish))

        max_fish = max(fish_power)
        max_shark = max(shark_power)

        # ugly code to make the power spectrum plot look neater
        fish_low_points = np.where(fish_power < self.GRAPH_CUTOFF_FRACTION * max_fish)[0]
        fish_cutoff = fish_low_points[np.where(fish_low_points > np.argmax(fish_power))[0][0]]

        shark_low_points = np.where(shark_power < self.GRAPH_CUTOFF_FRACTION * max_shark)[0]
        shark_cutoff = shark_low_points[np.where(shark_low_points > np.argmax(shark_power))[0][0]]

        plot_cutoff = max(fish_cutoff, shark_cutoff)
        return (freqs[0:plot_cutoff], fish_power[0:plot_cutoff], shark_power[0:plot_cutoff])

    def plot(self):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
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

        freqs, fish, shark = self.get_power_spectrum()
        ax3.plot(freqs, fish)
        ax3.plot(freqs, shark)
        ax3.set_xlabel("Frequency")
        ax3.set_ylabel("Power")
        ax3.set_title("Power Spectrum")

        plt.tight_layout(w_pad=-2)
        plt.show()
