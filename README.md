# papal

A playground for mathematical visualization and graphics, featuring:

- **Python/Matplotlib**: Plotting and exploring mathematical surfaces and toy models in 3D.

## Features

- 3D plotting scripts for:
  - Klein bottle
  - Möbius strip
  - Boy's surface
  - Enneper surface
  - Roman surface
  - Torus
  - Whitney umbrella
  - Schwarz P surface
  - Gyroid
  - Helicoid
  - Catenoid
  - Cross-cap
  - Dini’s surface
  - Scherk’s minimal surface

## Setup

1. (Recommended) Create a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run any math toy script, e.g.:
   ```sh
   python klein_bottle.py
   python mobius_strip.py
   # ...etc
   ```

## Project Structure

```
papal/
├── klein_bottle.py     # Python Klein bottle plot
├── mobius_strip.py     # Python Möbius strip plot
├── boys_surface.py     # Boy's surface
├── enneper_surface.py  # Enneper surface
├── roman_surface.py    # Roman surface
├── torus.py            # Torus
├── whitney_umbrella.py # Whitney umbrella
├── schwarz_p_surface.py# Schwarz P surface
├── gyroid.py           # Gyroid
├── helicoid.py         # Helicoid
├── catenoid.py         # Catenoid
├── cross_cap.py        # Cross-cap
├── dinis_surface.py    # Dini’s surface
├── scherk_minimal.py   # Scherk’s minimal surface
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

## Notes

- For matplotlib 3D plots, you may need `python3-tk` or `PyQt5` for interactive windows.
- All scripts are self-contained and can be run independently.
- Contributions and new math toys are welcome!
