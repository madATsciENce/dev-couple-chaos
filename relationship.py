# relationship.py

import random
import time
from feelings.hugs import HugService

# Simulating import of other systems (pretend they exist)
# from feelings.apology_handler import ApologyManager
# from feelings.argue_detector import ArgumentDetector
# from feelings.trust_building import TrustBot

class Relationship:
    def __init__(self):
        self.trust_score = 100
        self.happiness = 100
        self.fights = 0
        self.hug_service = HugService()

    def simulate_day(self):
        print("\n💬 New Day Simulation Starting...\n")
        
        # Random chance of an argument
        if random.random() < 0.3:
            self.handle_argument()

        # Random chance of random kiss
        if random.random() < 0.5:
            self.receive_random_kiss()

        # Healing over time
        self.hug_service.send_hug()
        self.trust_score = min(self.trust_score + 2, 100)
        self.happiness = min(self.happiness + 3, 100)
        
        print(f"❤️ Trust Score: {self.trust_score}")
        print(f"😊 Happiness Level: {self.happiness}")

    def handle_argument(self):
        print("🔥 Argument detected!")
        self.trust_score -= random.randint(10, 25)
        self.happiness -= random.randint(5, 15)
        self.fights += 1
        print("💔 Trust & happiness decreased!")
        
        if self.trust_score < 70:
            print("🤖 Triggering Trust Building Bot...")
            # TrustBot.repair()

    def receive_random_kiss(self):
        print("💋 Received a random kiss! Happiness boosted!")
        self.happiness += 5

    def status(self):
        return {
            "trust_score": self.trust_score,
            "happiness": self.happiness,
            "fights": self.fights
        }

if __name__ == "__main__":
    my_relationship = Relationship()
    for day in range(5):
        print(f"🗓️ Day {day+1}")
        my_relationship.simulate_day()
        time.sleep(1)
