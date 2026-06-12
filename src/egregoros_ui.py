import subprocess
import os
import sys
from src.egregoros_markov import MarkovGenerator

class EgregorosUI:
    def __init__(self):
        self.status = "READY"
        self.running = True
        self.markov = MarkovGenerator("/storage/emulated/0/RootBase/voice-cloner/profiles/lancy_lough.json")

    def display_header(self):
        print(f"\n--- EGREGOROS TUI | STATUS: {self.status} ---")

    def run(self):
        while self.running:
            self.display_header()
            print("[1] Run Synthesis")
            print("[5] Generate Behavioral Phrase")
            print("[6] OSINT URL Audio Ingestion")
            print("[7] Terminate Console Link")
            
            choice = input("Select option [1-7]: ").strip()
            
            if choice == '1':
                print("Running synthesis...")
            elif choice == '5':
                phrase = self.markov.generate()
                print(f"[EGREGOROS] Generated: {phrase}")
                # Placeholder for auto-passing to synthesis engine
            elif choice == '6':
                url = input("Enter URL: ")
                filename = input("Filename: ")
                subprocess.Popen(["python3", "tools/egregoros_scraper.py", url, filename])
            elif choice == '7':
                self.running = False

if __name__ == "__main__":
    ui = EgregorosUI()
    ui.run()
