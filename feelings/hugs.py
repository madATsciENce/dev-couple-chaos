import time
import random

class HugDistributor:
    def __init__(self, recipient):
        self.recipient = recipient
        self.hug_types = ["Bear Hug 🐻", "Side Hug 🤗", "Virtual Hug 💻", "Back Hug 😳"]

    def deliver_hug(self):
        hug = random.choice(self.hug_types)
        print(f"Delivering {hug} to {self.recipient}... 🤍")
        time.sleep(1)
        print("Hug successfully delivered! ✨")

if __name__ == "__main__":
    bae = HugDistributor("My Love")
    while True:
        bae.deliver_hug()
        time.sleep(random.randint(3,5))  # infinite loop of hugs
