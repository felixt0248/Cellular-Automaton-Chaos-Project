import yaml

from wator import WaTor

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    w = WaTor(config["starting_params"])
    w.simulate_n_steps(config["simulation_steps"])

    print("remaining fish:   ", w.n_fish)
    print("remaining sharks: ", w.n_shark)

if __name__ == "__main__":
    main()
