# Cellular Automaton Chaos Project

A very cool project about chaos in cellular automata by Anna and Felix!

## About

Originally described by Alexander K. Dewdney, WaTor is a simple predator-prey simulation set on the surface of a toroidal water world. Only fish and sharks inhabit the world and they follow the behaviours outlined below.

- Fish:
    - If there are any adjacent unoccupied cells, move randomly to one of them.
    - If the fish has lived long enough, leave behind a new fish after moving.
- Sharks:
    - If there are fish adjacent, move to a random one, eat it and gain energy.
    - If no fish are adjacent but there are still unoccupied cells, move randomly to one of them and lose energy.
    - If while moving, the shark has energy above a threshold, reproduce.
    - If the shark has energy below a threshold, die.

We aim to use this simple simulation idea to investigate how the world size impacts oscillatory behaviours of the system.

## Usage

Make sure all requirements are installed with
```bash
pip install -r requirements.txt
```

To run the simulation run
```bash
python3 simulate.py
```

The simulation parameters can be adjusted in `config.yaml`.

## Sample Output

Here is an example simulation on a 200x200 grid starting with 1000 fish and 1000 sharks over 500 time steps.

https://github.com/user-attachments/assets/12b16681-0cee-43f2-a6c4-ef46b4e61dc4

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/e8d1068e-2c03-47f9-b52b-2aa6204687ca" />

## Notes

I think we should change the plural of shark to shark as opposed to sharks.
