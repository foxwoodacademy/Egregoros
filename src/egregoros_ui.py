import os
import sys
import time
import subprocess
import logging
import asyncio
import json

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from egregoros_engine import VoiceClonerMatrix
from egregoros_profiler import EgregorosBehavioralProfiler

logging.basicConfig(level=logging.ERROR)

class EgregorosTUI:
    def __init__(self):
        self.matrix = VoiceClonerMatrix()
        self.profiler = EgregorosBehavioralProfiler()
        self.target_name = "Lancy Lough"
        self.sample_path = "/storage/emulated/0/RootBase/voice-cloner/samples/lancy_source.mp3"
        self.output_path = "lancy_clone.wav"
        self.base_dir = "/storage/emulated/0/RootBase/voice-cloner"

    def clear_screen(self):
        os.system('clear')

    def draw_header(self):
        # Dynamically check if the background ingestor is running
        ingestor_active = False
        try:
            pgrep_check = subprocess.check_output(["pgrep", "-f", "egregoros_ingest.py"])
            if pgrep_check:
                ingestor_active = True
        except subprocess.CalledProcessError:
            pass

        print("================================================================")
        print("   AN/VQX-9 EGREGOROS // TARGET ACQUISITION & SYNTHESIS TUI     ")
        print("   CURRENT WORKBENCH VECTOR: MONITORING MAYOR / WORKBENCH CHAIR ")
        print("================================================================")
        print(f" TARGET PROFILE:  [{self.target_name}]")
        if ingestor_active:
            print(" STATUS MATRIX:   [+] VOICE PRINT: ACTIVE (SECURE INGESTION RUNNING)")
        else:
            print(f" VOICE PRINT:     {self.sample_path if os.path.exists(self.sample_path) else 'NOT ACQUIRED (MISSING)'}")
        print("================================================================")

    def record_target_audio(self):
        self.clear_screen()
        self.draw_header()
        print("\n [!] INITIALIZING HARDWARE AUDIO STREAM INTERCEPT...")
        duration = input("\n Enter capture duration in seconds (Default: 10): ") or "10"
        os.makedirs(os.path.dirname(self.sample_path), exist_ok=True)
        print(f"\n [*] RECORDING ACTIVE... Speak clearly into the node array for {duration} seconds.")
        cmd = f"termux-microphone-record -f {self.sample_path} -l {duration}"
        subprocess.run(cmd, shell=True)
        time.sleep(int(duration) + 1)
        if os.path.exists(self.sample_path) and os.path.getsize(self.sample_path) > 0:
            print("\n [+] SUCCESS: Audio print captured and logged.")
        else:
            print("\n [!] FAILURE: Android restricted background recording access.")
        time.sleep(2)

    def process_target_profile(self):
        self.clear_screen()
        self.draw_header()
        print("\n [*] RUNNING ADAPTIVE BEHAVIORAL PROFILE PASS...")
        if not os.path.exists(self.sample_path):
            print("\n [!] ERROR: No target voice print found. Run option 1 first.")
        else:
            profile = self.matrix.analyze_audio_prana(self.sample_path)
            if profile:
                print("\n --- FREQUENCY RESULTS METRICS ---")
                print(f"  Root Mean Square (Energy): {profile.get('rms')}")
                print(f"  Decibel Amplitude Matrix:  {profile.get('decibels'):.2f} dBFS")
                print(f"  Acoustic Payload Length:   {profile.get('duration_ms')} ms")
            else:
                print("\n [!] Analysis module rejected the audio container structure.")
        input("\n Press Enter to return to operational console...")

    def trigger_ingestion_sweep(self):
        self.clear_screen()
        self.draw_header()
        print("\n [*] ENFORCING BACKGROUND HARVESTING COMPARTMENT...")
        
        # Guard clause: Check if already running to prevent zombie threads
        try:
            subprocess.check_output(["pgrep", "-f", "egregoros_ingest.py"])
            print("\n [!] ALERT: An ingestion daemon process is already active in this sandbox.")
            time.sleep(2)
            return
        except subprocess.CalledProcessError:
            pass

        ingest_script = os.path.join(self.base_dir, "tools/egregoros_ingest.py")
        print(f" Spawning background loop for path alignment: {ingest_script}")
        
        # Fixed absolute path execution layer
        subprocess.Popen(["python3", ingest_script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("\n [+] Ingestion sweep background matrix launched successfully.")
        time.sleep(1.5)

    def generate_cloned_payload(self):
        self.clear_screen()
        self.draw_header()
        print(" 1. Enter manual text string inject")
        print(" 2. Auto-generate NLP hypnotic pattern clone")
        print(" 3. Load pre-compiled behavioral script template")
        mode = input("\n Select generation matrix [1-3]: ")

        phrase_to_run = ""
        if mode == "2":
            db = self.profiler.data
            crutch = db.get("speech_patterns", {}).get("crutch_words", ["fundamentally"])[0].capitalize()
            anchor = db.get("neuro_linguistic_markers", {}).get("hypnotic_anchors", ["Look at the baseline blueprint here"])[0]
            phrase = db.get("speech_patterns", {}).get("common_phrases", ["Refactor the ink, clean the lines."])[0]
            phrase_to_run = f"{crutch}, if you {anchor.lower()}, you will see how we {phrase.lower()}"
        elif mode == "3":
            templates = self.profiler.data.get("script_templates", [])
            if not templates:
                print("\n [!] No templates found in database profile.")
                time.sleep(1)
                return
            print("\n --- AVAILABLE BEHAVIORAL TEMPLATES ---")
            for idx, t in enumerate(templates):
                print(f"  {idx + 1}. [{t['name']}] -> {t['text'][:50]}...")
            t_choice = input("\n Select template number: ")
            try:
                phrase_to_run = templates[int(t_choice) - 1]["text"]
            except:
                print("[!] Invalid selection.")
                time.sleep(1)
                return
        else:
            phrase_to_run = input("\n Enter custom text string for synthesis:\n >> ")

        if not phrase_to_run:
            return

        print(f"\n [*] TARGET INJECTION PHRASE:\n >> \"{phrase_to_run}\"")
        print("\n [*] Initiating proxy stream compilation...")
        asyncio.run(self.matrix.synthesize_voice_proxy(
            text=phrase_to_run, 
            output_filename=self.output_path, 
            custom_voice="en-GB-RyanNeural"
        ))
        print(f"\n [+] Payload compiled cleanly: outputs/{self.output_path}")
        input("\n Press Enter to return to operational console...")

    def run_loop(self):
        while True:
            self.clear_screen()
            self.draw_header()
            print(" 1. Intercept Voice Sample (Mic Capture)")
            print(" 2. Profile Audio Frequency Parameters")
            print(" 3. Compile Synthetic Target Payload")
            print(" 4. Initialize Temp Ingestion Sweep (Daemon)")
            print(" 5. Terminate Console Link (Exit)")
            print("================================================================")
            choice = input(" Select vector option [1-5]: ")

            if choice == "1":
                self.record_target_audio()
            elif choice == "2":
                self.process_target_profile()
            elif choice == "3":
                self.generate_cloned_payload()
            elif choice == "4":
                self.trigger_ingestion_sweep()
            elif choice == "5":
                self.clear_screen()
                break

if __name__ == "__main__":
    tui = EgregorosTUI()
    tui.run_loop()
