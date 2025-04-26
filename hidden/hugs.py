# hugs.py

class Hug:
    def __init__(self, recipient):
        self.recipient = recipient
        self.hug_strength = 0

    def initiate_hug(self):
        print(f"Initiating hug sequence for {self.recipient}...")
        self.hug_strength += 1
        if self.hug_strength >= 5:
            print("Warning: Hug overflow detected! Maximum love reached ❤️.")
        else:
            print(f"Hug level: {self.hug_strength}")

    def infinite_hugs(self):
        while True:
            self.initiate_hug()

if __name__ == "__main__":
    soulmate = Hug("You 💖")
    try:
        soulmate.infinite_hugs()
    except KeyboardInterrupt:
        print("\nHugging manually... 🫂")
