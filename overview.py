import os
import numpy as np
from concurrent import futures
from matplotlib import pyplot as plt
from matplotlib import animation

class Overview:
    GRAPH_CUTOFF_FRACTION = 0.001
    PLOT_PATH = "data/tempplots"
    ANIM_PATH = "data/tempanimations"

    def __init__(self, name, data):
        self.ensure_paths()
        self.fish, self.shark, self.colour_matrices = map(list, zip(*data))
        self.t = np.arange(0, len(self.fish), 1)
        self.name = name

    @staticmethod
    def gen_parallel(overviews, settings):
        with futures.ProcessPoolExecutor() as executor:
            fs = [executor.submit(Overview.gen, overview, settings) for overview in overviews]
            [f.result() for f in futures.as_completed(fs)]

    def gen(self, settings):
        self.uniquify_name()
        if any(self.colour_matrices):
            self.animate()
        if settings["gen_plots"]:
            self.plot()
        if settings["print_results"]:
            self.print_results()

    def uniquify_name(self):
        if "u" not in self.name:
            self.name += f"n{len(self.fish)}u{self.unique_suffix()}"

    def unique_suffix(self):
        existing = list(set([f.split(".")[0] for f in os.listdir(self.PLOT_PATH)]) | set([f.split(".")[0] for f in os.listdir(self.ANIM_PATH)]))
        existing_suffixes = [int(f.split("u")[1]) for f in existing]
        if len(existing_suffixes) == 0:
            suffix = 1
        else:
            suffix = 1 + max(existing_suffixes)
        return str(suffix).zfill(3)

    def ensure_paths(self):
        os.makedirs(self.PLOT_PATH, exist_ok=True)
        os.makedirs(self.ANIM_PATH, exist_ok=True)

    def print_results(self):
        print("fish std: \t", np.std(self.fish))
        print("shark std:\t", np.std(self.shark))

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

    def animate(self):
        fig, ax = plt.subplots()
        artists = [[ax.matshow(M)] for M in self.colour_matrices]
        anim = animation.ArtistAnimation(fig=fig, artists=artists, interval=10)
        anim.save(f"{self.ANIM_PATH}/{self.name}.mp4", writer="ffmpeg", fps=30)

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

        fig.tight_layout()
        fig.savefig(f"{self.PLOT_PATH}/{self.name}.png")
