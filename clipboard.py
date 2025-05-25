import pyperclip
import time
import threading
import json
import os

HISTORY_FILE = "history.json"

class clipboarwatcher(threading.Thread):
    def __init__(self, callback, pause=1.0):
        super().__init__(daemon=True)
        self.callback = callback
        self.last_clipboard = ""
    
    def run(self):
        while True:
            text = pyperclip.paste()
            if text != self.last_clipboard:
                self.last_clipboard = text
                self.callback(text)
            time.sleep(1) #check every second

def save_to_history(text):
    history = load_history()
    if text not in history:
        history.insert(0, text) # insert new text at top 
        history = history[:500]
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f)

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return []

## test the code 
#
#if __name__ == "__main__":
#    def on_new_clipboard_text(text):
#        print(f"New Clipboard content: {text}")
#        save_to_history(text)
#
#watcher = clipboarwatcher(on_new_clipboard_text, pause=1.0)
#watcher.start()
#
#try:
#    while True:
#        time.sleep(1)
#except KeyboardInterrupt:
#    print("Stopped!")


