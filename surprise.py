#!/usr/bin/env python3
"""
🎉 SURPRISE! 🎉
A delightful digital companion that brings joy to your terminal!
"""

import random
import time
import sys
from datetime import datetime

class DigitalPet:
    """A friendly digital pet that loves to interact!"""
    
    def __init__(self, name="Rocky"):
        self.name = name
        self.mood = random.choice(["happy", "excited", "playful", "curious"])
        self.energy = 100
        self.friendship = 50
        self.birthday = datetime.now()
        
    def animate_text(self, text, delay=0.03):
        """Print text with a typing animation effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def show_face(self):
        """Display the pet's current mood as ASCII art"""
        faces = {
            "happy": """
    ╔═══════════╗
    ║  ^     ^  ║
    ║    ╰─╯    ║
    ║  ╰─────╯  ║
    ╚═══════════╝
            """,
            "excited": """
    ╔═══════════╗
    ║  O     O  ║
    ║    ╰─╯    ║
    ║  ╰─────╯  ║
    ╚═══════════╝
            """,
            "playful": """
    ╔═══════════╗
    ║  ~     ~  ║
    ║    ╰─╯    ║
    ║  ╰─────╯  ║
    ╚═══════════╝
            """,
            "curious": """
    ╔═══════════╗
    ║  o     o  ║
    ║    ╰─╯    ║
    ║  ╰─────╯  ║
    ╚═══════════╝
            """
        }
        print(faces.get(self.mood, faces["happy"]))
    
    def tell_joke(self):
        """Tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't programmers like nature? It has too many bugs!",
            "How do you comfort a JavaScript bug? You console it!",
        ]
        joke = random.choice(jokes)
        self.animate_text(f"\n{self.name}: *clears throat*\n")
        time.sleep(0.5)
        self.animate_text(f"{self.name}: {joke}")
        time.sleep(1)
        self.animate_text(f"{self.name}: *giggles* 😄\n")
        self.friendship += 5
        self.mood = random.choice(["happy", "excited"])
    
    def play_game(self):
        """Play a simple number guessing game"""
        self.animate_text(f"\n{self.name}: Let's play a game! I'm thinking of a number between 1 and 10...")
        secret = random.randint(1, 10)
        
        for attempt in range(3):
            try:
                guess = int(input(f"{self.name}: Your guess (attempt {attempt + 1}/3): "))
                if guess == secret:
                    self.animate_text(f"\n{self.name}: 🎉 You got it! You're amazing!")
                    self.friendship += 10
                    self.mood = "excited"
                    return
                elif guess < secret:
                    self.animate_text(f"{self.name}: Too low! Try again!")
                else:
                    self.animate_text(f"{self.name}: Too high! Try again!")
            except ValueError:
                self.animate_text(f"{self.name}: That's not a number! Try again!")
        
        self.animate_text(f"\n{self.name}: The number was {secret}! Better luck next time! 😊")
        self.friendship += 3
    
    def show_fortune(self):
        """Display a random fortune"""
        fortunes = [
            "A journey of a thousand miles begins with a single step.",
            "Good things come to those who wait.",
            "The best time to plant a tree was 20 years ago. The second best time is now.",
            "You will find great success in your coding endeavors!",
            "A surprise is waiting for you around the corner!",
            "Your creativity will lead you to amazing places!",
            "Today is a perfect day to learn something new!",
            "Great things never come from comfort zones!",
        ]
        fortune = random.choice(fortunes)
        self.animate_text(f"\n{self.name}: *gazing into crystal ball* 🔮")
        time.sleep(1)
        self.animate_text(f"{self.name}: Your fortune: {fortune}\n")
        self.friendship += 3
    
    def dance(self):
        """Perform a fun ASCII dance animation"""
        if self.energy < 10:
            self.animate_text(f"\n{self.name}: *yawns* I'm too tired to dance right now... 😴")
            self.animate_text(f"{self.name}: Maybe after I rest a bit!\n")
            return
        
        self.animate_text(f"\n{self.name}: Let me show you my moves! 💃\n")
        dance_frames = [
            "  (\\_/)  ",
            "  (o_o)  ",
            "  (^_^)  ",
            "  (\\_/)  ",
        ]
        for _ in range(3):
            for frame in dance_frames:
                print(f"\r{frame}", end="", flush=True)
                time.sleep(0.3)
        print("\n")
        self.animate_text(f"{self.name}: Ta-da! 🎉\n")
        self.energy = max(0, self.energy - 10)  # Ensure energy doesn't go below 0
        self.friendship += 5
        self.mood = "excited"
    
    def show_stats(self):
        """Display pet statistics"""
        age = (datetime.now() - self.birthday).total_seconds()
        # Ensure energy is within valid bounds for display
        energy_display = max(0, min(100, self.energy))
        energy_bars = max(0, energy_display // 10)
        
        print(f"\n{'='*40}")
        print(f"📊 {self.name}'s Stats")
        print(f"{'='*40}")
        print(f"Name: {self.name}")
        print(f"Mood: {self.mood.capitalize()} {self._get_mood_emoji()}")
        print(f"Energy: {'█' * energy_bars} {energy_display}%")
        print(f"Friendship: {'❤️' * (self.friendship // 20)} {self.friendship}/100")
        print(f"Age: {int(age)} seconds old")
        print(f"{'='*40}\n")
    
    def _get_mood_emoji(self):
        """Get emoji for current mood"""
        emojis = {
            "happy": "😊",
            "excited": "🤩",
            "playful": "😄",
            "curious": "🤔"
        }
        return emojis.get(self.mood, "😊")
    
    def interact(self):
        """Main interaction loop"""
        self.animate_text(f"\n{'='*50}")
        self.animate_text(f"🌟 Welcome! I'm {self.name}, your digital pet! 🌟")
        self.animate_text(f"{'='*50}\n")
        
        while True:
            self.show_face()
            print(f"\n{self.name}: What would you like to do?")
            print("1. Tell me a joke")
            print("2. Play a game")
            print("3. Show me a fortune")
            print("4. Watch me dance")
            print("5. Check my stats")
            print("6. Exit")
            
            choice = input("\nYour choice: ").strip()
            
            if choice == "1":
                self.tell_joke()
            elif choice == "2":
                self.play_game()
            elif choice == "3":
                self.show_fortune()
            elif choice == "4":
                self.dance()
            elif choice == "5":
                self.show_stats()
            elif choice == "6":
                self.animate_text(f"\n{self.name}: Aww, do you have to go? 😢")
                time.sleep(0.5)
                self.animate_text(f"{self.name}: It was so much fun hanging out with you!")
                self.animate_text(f"{self.name}: Come back soon! Bye-bye! 👋\n")
                break
            else:
                self.animate_text(f"{self.name}: Hmm, I didn't understand that. Let's try again!")
            
            # Random mood change
            if random.random() < 0.3:
                self.mood = random.choice(["happy", "excited", "playful", "curious"])
            
            time.sleep(0.5)


def main():
    """Main entry point"""
    print("\n" + "="*50)
    print("🎉 SURPRISE! 🎉".center(50))
    print("="*50)
    
    pet_name = input("\nWhat would you like to name your pet? (or press Enter for 'Rocky'): ").strip()
    if not pet_name:
        pet_name = "Rocky"
    
    pet = DigitalPet(name=pet_name)
    pet.interact()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing! Goodbye!")
    except Exception as e:
        print(f"\n❌ Oops! Something went wrong: {e}")
