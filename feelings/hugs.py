# feelings/hugs.py

import random

class HugService:
    def __init__(self):
        self.hug_count = 0

    def send_hug(self):
        hugs = ["Bear Hug 🤗", "Quick Hug 🫂", "Tight Hug 🧸", "Back Hug 🥰"]
        chosen_hug = random.choice(hugs)
        print(f"[HUG SERVICE]: Sending {chosen_hug}")
        self.hug_count += 1
