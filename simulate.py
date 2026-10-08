from wator import WaTor

def main():
    w = WaTor(4, 4, 3, 3, 10, 10) # example WaTor world
    print(w.grid)
    w.simulate_n_steps(100)
    print(w.grid)

if __name__ == "__main__":
    main()
