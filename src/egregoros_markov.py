import json
import random
import os

class MarkovGenerator:
    def __init__(self, profile_path):
        with open(profile_path, 'r') as f:
            data = json.load(f)
        phrases = data['speech_patterns']['common_phrases']
        self.bigrams = self._build_bigrams(phrases)

    def _build_bigrams(self, phrases):
        bigrams = {}
        for phrase in phrases:
            words = phrase.split()
            for i in range(len(words) - 1):
                word = words[i]
                next_word = words[i+1]
                if word not in bigrams:
                    bigrams[word] = []
                bigrams[word].append(next_word)
        return bigrams

    def generate(self, length=10):
        if not self.bigrams: return "Error."
        word = random.choice(list(self.bigrams.keys()))
        output = [word]
        for _ in range(length):
            if word in self.bigrams:
                word = random.choice(self.bigrams[word])
                output.append(word)
            else:
                break
        return " ".join(output) + "."
