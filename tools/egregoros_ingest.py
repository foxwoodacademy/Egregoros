import os
import time
from pydub import AudioSegment

TEMP_DIR = "/storage/emulated/0/RootBase/voice-cloner/temp/"
TARGET_FILE = "/storage/emulated/0/RootBase/voice-cloner/samples/lancy_source.mp3"
TARGET_RATE = 44100

def ingest():
    print("[EGREGOROS] Automated Ingestor Online. Monitoring /temp/")
    while True:
        for filename in os.listdir(TEMP_DIR):
            if filename.lower().endswith(('.mp3', '.wav', '.m4a')):
                path = os.path.join(TEMP_DIR, filename)
                print(f"[EGREGOROS] Ingesting: {filename}")
                
                try:
                    audio = AudioSegment.from_file(path)
                    # Set frame rate and export without tags (metadata stripping)
                    audio = audio.set_frame_rate(TARGET_RATE)
                    audio.export(TARGET_FILE, format="mp3", tags={})
                    
                    os.remove(path)
                    print(f"[EGREGOROS] Processed and secured to: {TARGET_FILE}")
                except Exception as e:
                    print(f"[EGREGOROS] Error processing {filename}: {e}")
        time.sleep(5)

if __name__ == "__main__":
    ingest()
