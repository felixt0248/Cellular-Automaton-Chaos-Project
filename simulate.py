import yaml

from wator import WaTor
from visualisation import plot_overview

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    w = WaTor(config["starting_params"])
    overview = w.simulate_n_steps(config["simulation_params"])
    plot_overview(overview)

if __name__ == "__main__":
    main()
