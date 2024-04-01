import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class HTMLChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".html"):
            print("HTML file modified. Reloading Gunicorn...")
            subprocess.run(["pkill", "-HUP", "-f", "gunicorn"])

def run_with_watchdog():
    event_handler = HTMLChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()
    
    try:
        subprocess.run(["gunicorn", "-b 0.0.0.0:80", "app:app", "--reload"])
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    run_with_watchdog()
