from gui import ClippboardApp
from clipboard import clipboarwatcher

if __name__ == "__main__":
    app = ClippboardApp()

    watcher = clipboarwatcher(app.add_to_history)
    watcher.start()

    app.mainloop()