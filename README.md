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

To run the simulation run
```bash
python3 simulate.py
```

The simulation parameters can be adjusted in `config.yaml`.

## Notes

I think we should change the plural of shark to shark as opposed to sharks.
