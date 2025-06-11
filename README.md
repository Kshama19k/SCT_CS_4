# Task 04 - Basic Keylogger Program

## 📌 Objective

Create a basic keylogger program in Python that:
- Records and logs keystrokes.
- Saves the logged keys into a file for later review.

## 🛠️ Requirements

- Python 3.x
- `pynput` library for keyboard event listening


# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
