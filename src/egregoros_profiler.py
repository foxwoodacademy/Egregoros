import os
import json
import logging

logger = logging.getLogger("EGREGOROS.Profiler")

class EgregorosBehavioralProfiler:
    def __init__(self, profile_path="/storage/emulated/0/RootBase/voice-cloner/profiles/lancy_lough.json"):
        self.profile_path = profile_path
        self.data = self._load_profile()

    def _load_profile(self):
        if not os.path.exists(self.profile_path):
            logger.error(f"Target behavioral ledger missing at: {self.profile_path}")
            return {}
        with open(self.profile_path, 'r') as f:
            return json.load(f)

    def _save_profile(self):
        try:
            with open(self.profile_path, 'w') as f:
                json.dump(self.data, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Failed to write changes to target ledger: {e}")
            return False

    def parse_transcript_prana(self, text_blob):
        """
        Scans a raw input transcript text blob.
        Tags NLP markers, isolates potential new catchphrases, 
        and extracts behavioral patterns.
        """
        logger.info("Initiating syntax breakdown matrix...")
        text_lower = text_blob.lower()
        analysis_report = {
            "matched_phrases": [],
            "nlp_trigger_hits": 0,
            "detected_crutch_words": {},
            "psychological_tone": "Neutral"
        }

        # 1. Check for known phrase signatures
        patterns = self.data.get("speech_patterns", {})
        for phrase in patterns.get("common_phrases", []):
            if phrase.lower() in text_lower:
                analysis_report["matched_phrases"].append(phrase)

        # 2. Count crutch words to track cognitive pacing deviations
        for word in patterns.get("crutch_words", []):
            count = text_lower.count(word.lower())
            if count > 0:
                analysis_report["detected_crutch_words"][word] = count

        # 3. Calculate neuro-linguistic trigger proximity
        nlp = self.data.get("neuro_linguistic_markers", {})
        for anchor in nlp.get("hypnotic_anchors", []):
            if anchor.lower() in text_lower:
                analysis_report["nlp_trigger_hits"] += 1

        # Determine emotional orientation based on syntax complexity
        if analysis_report["nlp_trigger_hits"] > 0:
            analysis_report["psychological_tone"] = "High Hypnotic Authority"
        elif len(analysis_report["matched_phrases"]) > 1:
            analysis_report["psychological_tone"] = "Standard Target Cadence"

        return analysis_report

    def learn_new_phrase(self, exact_phrase):
        """Appends a newly monitored verbal habit to the database ledger."""
        if not exact_phrase:
            return False
        
        phrases = self.data.get("speech_patterns", {}).get("common_phrases", [])
        if exact_phrase not in phrases:
            phrases.append(exact_phrase)
            self.data["speech_patterns"]["common_phrases"] = phrases
            self._save_profile()
            logger.info(f"Learned new behavioral syntax rule: '{exact_phrase}'")
            return True
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    profiler = EgregorosBehavioralProfiler()
    
    # Run a test parse sample
    sample_intercept = "Fundamentally, if you look at the baseline blueprint here, you can see how we refactor the ink and clean the lines."
    report = profiler.parse_transcript_prana(sample_intercept)
    print("\n--- SAMPLE INTERCEPT PARSE MATRIX RESULT ---")
    print(json.dumps(report, indent=2))
