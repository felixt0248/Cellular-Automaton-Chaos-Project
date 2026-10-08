from wator import WaTor

def main():
    w = WaTor(8, 8, 1, 1, {"initial_age": 0, "time_to_reproduce": 15}, {"initial_energy": 1, "max_energy": 1, "energy_gain": 0.15, "energy_loss": 0.04, "energy_to_reproduce": 0.98}) # example WaTor world
    w.simulate_n_steps(100)
    print(w.n_fish)
    print(w.n_shark)

if __name__ == "__main__":
    main()
