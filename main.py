import time
from pathlib import Path

VERSION = Path(__file__).with_name("VERSION").read_text().strip()

if __name__ == "__main__":
    print(f"Hello from Jetson! Version: {VERSION}", flush=True)

    while True:
        print(f"Running version {VERSION}...", flush=True)
        time.sleep(1)
