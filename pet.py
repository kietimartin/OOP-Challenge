class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)  # Ensure hunger doesn't go below 0
            self.happiness = min(10, self.happiness + 1)  # Cap happiness at 10
        else:
            self.happiness = min(10, self.happiness + 1)
        return f'{self.name} is eating🍚...'

    def sleep(self):
        if self.energy < 10:
            self.energy = min(10, self.energy + 5)  # Cap energy at 10
        return f'{self.name} is sleeping...'

    def play(self):
        self.energy = max(0, self.energy - 2)  # Ensure energy doesn't go below 0
        self.happiness = min(10, self.happiness + 2)  # Cap happiness at 10
        self.hunger = min(10, self.hunger + 1)  # Cap hunger at 10
        return f'{self.name} is playing🐕...'

    def train(self, trick):
        if trick not in self.tricks:  # Avoid duplicate tricks
            self.tricks.append(trick)

    def show_tricks(self):
        return self.tricks

    def get_status(self):
        return f"{self.name}'s current status🐕:\n" \
                f"Hunger: {self.hunger}\n" \
                f"Energy: {self.energy}\n" \
                f"Happiness: {self.happiness}\n" \
                f"Tricks: {', '.join(self.tricks)}"