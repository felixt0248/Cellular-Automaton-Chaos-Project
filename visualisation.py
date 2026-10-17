import numpy as np
from matplotlib import pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 25,
    "mathtext.fontset": "cm",
})

def plot_overview(overview):
    fish, shark = map(list, zip(*overview))
    t = np.arange(0, len(fish), 1)

    fig, ax = plt.subplots()
    ax.plot(t, fish, label="Fish")
    ax.plot(t, shark, label="Sharks")
    ax.set_xlabel("Time")
    ax.set_ylabel("Population")
    ax.legend()

    plt.show()
