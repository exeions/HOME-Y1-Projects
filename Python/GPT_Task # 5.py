# Mini Arcade Game: Reaction Trainer (Windows-only)
import time
import random
import msvcrt
import os

HIGH_SCORE_FILE = "high_score.txt"

def get_high_score():
    """Return the best (lowest) saved reaction time as a float, or None if missing/invalid."""
    if not os.path.exists(HIGH_SCORE_FILE):
        return None
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            text = f.read().strip()
            if text == "":
                return None
            return float(text)
    except (ValueError, IOError):
        return None

def save_high_score(score):
    """Overwrite the high score file with the given score (float)."""
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(f"{score:.3f}")
    except IOError:
        print("Warning: could not save high score.")

def start():
    input("Press Enter to begin...")
    print("Get ready...")
    time_wait = random.randint(1,5)
    time.sleep(time_wait)

    print("GO!")

    # Clear any keypresses that happened before GO
    while msvcrt.kbhit():
        msvcrt.getch()

    start_time = time.time()

    # Wait for the FIRST keypress AFTER "GO!"
    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            end_time = time.time()
            break

    seconds = round(end_time - start_time, 3)
    print(f"You got a score of: {seconds} seconds")

    # High score logic: lower is better
    best = get_high_score()
    if best is None or seconds < best:
        save_high_score(seconds)
        print("New high score! Saved.")
    else:
        print(f"High score remains: {best:.3f} seconds")

def view_high_score():
    best = get_high_score()
    if best is None:
        print("No high score yet. Play a round to create one!")
    else:
        print(f"High score: {best:.3f} seconds")

def main():
    while True:
        print("=== Reaction Trainer ===\n" 
              "1. Start Game\n"
              "2. View High Score\n"
              "3. Quit\n")

        select_option = input("Select option: ").strip()
        if select_option == "1":
            start()
        elif select_option == "2":
            view_high_score()
        elif select_option == "3":
            print("Quitting program.")
            break
        else:
            print("Invalid option.\n")
        
if __name__ == "__main__":
    main()
