import yaml

from wator import WaTor
from overview import Overview

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    w = WaTor(config["starting_params"])
    w.simulate_n_worlds(config["simulation_params"])
    #overview = Overview(w.simulate_n_steps(config["simulation_params"]))
    #overview.show(config["overview_settings"])

if __name__ == "__main__":
    main()
