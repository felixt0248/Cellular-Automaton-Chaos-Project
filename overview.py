import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class Overview:
    GRAPH_CUTOFF_FRACTION = 0.001
    PLOT_PATH = "data/plots"
    ANIM_PATH = "data/animations"

    def __init__(self, name, data):
        self.ensure_paths()
        self.fish, self.shark, self.colour_matrices = map(list, zip(*data))
        self.t = np.arange(0, len(self.fish), 1)
        self.name = name

    def gen(self, settings):
        self.uniquify_name()
        self.get_power_spectrum()
        if any(self.colour_matrices):
            self.animate()
        if settings["gen_plots"]:
            self.plot()
        if settings["print_results"]:
            results = self.get_results()
        return results

    def uniquify_name(self):
        if "U" not in self.name:
            self.name += f"N{len(self.fish)}U{self.unique_suffix()}"

    def unique_suffix(self):
        existing = list(set([f.split(".")[0] for f in os.listdir(self.PLOT_PATH)]) | set([f.split(".")[0] for f in os.listdir(self.ANIM_PATH)]))
        existing_suffixes = [int(f.split("U")[1]) for f in existing]
        if len(existing_suffixes) == 0:
            suffix = 1
        else:
            suffix = 1 + max(existing_suffixes)
        return str(suffix).zfill(3)

    def ensure_paths(self):
        os.makedirs(self.PLOT_PATH, exist_ok=True)
        os.makedirs(self.ANIM_PATH, exist_ok=True)

    def get_results(self):
        extinction_time = len(self.fish) if (self.fish[-1] == 0 or self.shark[-1] == 0) else None
        return {
            "fish_std": np.std(self.fish),
            "shark_std": np.std(self.shark),
            "fish_peak_frequency": self.freqs[np.argmax(self.fish_power)],
            "fish_peak_amplitude": max(self.fish_power),
            "shark_peak_frequency": self.freqs[np.argmax(self.shark_power)],
            "shark_peak_amplitude": max(self.shark_power),
            "extinction_time": extinction_time
        }
         

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
        try:
            fish_cutoff = fish_low_points[np.where(fish_low_points > np.argmax(fish_power))[0][0]]
        except:
            fish_cutoff = -1

        shark_low_points = np.where(shark_power < self.GRAPH_CUTOFF_FRACTION * max_shark)[0]
        try:
            shark_cutoff = shark_low_points[np.where(shark_low_points > np.argmax(shark_power))[0][0]]
        except:
            shark_cutoff = -1

        plot_cutoff = max(fish_cutoff, shark_cutoff)
        self.freqs = freqs[0:plot_cutoff]
        self.fish_power = fish_power[0:plot_cutoff]
        self.shark_power = shark_power[0:plot_cutoff]

    def animate(self):
        fig, ax = plt.subplots()
        artists = [[ax.matshow(M)] for M in self.colour_matrices]
        anim = animation.ArtistAnimation(fig=fig, artists=artists, interval=10)
        anim.save(f"{self.ANIM_PATH}/{self.name}.mp4", writer="ffmpeg", fps=30)

    def plot(self):
        # make this neater later
        x = self.name.split("X")[1].split("Y")[0]
        y = self.name.split("Y")[1].split("F")[0]

        fig, ax = plt.subplots()
        ax.plot(self.t, self.fish, label="Fish")
        ax.plot(self.t, self.shark, label="Sharks")
        ax.set_xlabel("Time")
        ax.set_ylabel("Population")
        ax.set_title(f"Time Evolution of Populations {x}x{y}")
        ax.legend()
        fig.savefig(f"{self.PLOT_PATH}/time_{self.name}.png")
        ax.cla()

        ax.plot(self.fish, self.shark)
        ax.set_xlabel("Fish")
        ax.set_ylabel("Sharks")
        ax.set_title(f"Phase Diagram {x}x{y}")
        fig.savefig(f"{self.PLOT_PATH}/phase_{self.name}.png")
        ax.cla()

        ax.plot(self.freqs, self.fish_power)
        ax.plot(self.freqs, self.shark_power)
        ax.set_xlabel("Frequency")
        ax.set_ylabel("Power")
        ax.set_title(f"Power Spectrum {x}x{y}")
        fig.savefig(f"{self.PLOT_PATH}/freq_{self.name}.png")
        ax.cla()

    @staticmethod
    def print_means(results):
        extinctions = [result.pop("extinction_time") for result in results]
        if all(extinctions):
            average_extinction_time = np.mean(extinctions)
        elif any(extinctions):
            average_extinction_time = "partial survivorship"
        else:
            average_extinction_time = "no extinctions"
        print("average time until extinction: ", average_extinction_time)

        averages = np.mean([list(result.values()) for result in results], axis=0)
        print(dict(zip(results[0].keys(), averages)))
