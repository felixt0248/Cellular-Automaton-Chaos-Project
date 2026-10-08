from wator import WaTor

def main():
    w = WaTor(4, 4, 3, 3, {"initial_age": 0, "time_to_reproduce": 15}, {"initial_energy": 0, "max_energy": 1, "energy_gain": 0.15, "energy_loss": 0.04, "energy_to_reproduce": 0.98}) # example WaTor world
    print(w.grid)
    w.simulate_n_steps(100)
    print(w.grid)

if __name__ == "__main__":
    main()
