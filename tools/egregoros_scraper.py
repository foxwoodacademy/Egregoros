import urllib.request
import os
import sys

TEMP_DIR = "/storage/emulated/0/RootBase/voice-cloner/temp"

def scrape(url, filename):
    print(f"[EGREGOROS] Scraping: {url}")
    try:
        path = os.path.join(TEMP_DIR, filename)
        urllib.request.urlretrieve(url, path)
        print(f"[EGREGOROS] Streamed to {path}")
    except Exception as e:
        print(f"[EGREGOROS] Scrape Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        scrape(sys.argv[1], sys.argv[2])
