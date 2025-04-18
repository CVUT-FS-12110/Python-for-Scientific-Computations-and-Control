# Pendulum Simulator with PID Control

This project simulates a cart-pendulum system using Python and PyGame.  
The provided PID controller leads a cart to desired position x. You can interactively add additional force using left and right keys.

---

## Installation

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Run the Simulation

```bash
python simulator.py
```

---

## Project Structure

- `simulator.py` – Main file with PyGame simulation
- `utils.py` – Contains model equations, solver, and PID controller
- `requirements.txt` – List of required packages

---
