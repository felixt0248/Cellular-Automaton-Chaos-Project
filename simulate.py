import yaml

from wator import WaTor
from overview import Overview

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    w = WaTor(config["starting_params"])
    overviews = [Overview(name, overview) for name, overview in w.simulate_n_worlds(config["simulation_params"])]
    Overview.gen_parallel(overviews, config["overview_settings"])

if __name__ == "__main__":
    main()
