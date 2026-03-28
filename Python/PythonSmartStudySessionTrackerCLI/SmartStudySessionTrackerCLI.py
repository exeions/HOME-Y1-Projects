#~ Project: Smart Study Session Tracker (CLI App)
## May make a web-app for soon.

# CLI app that tracks study sessions, stores them in JSON, and provides simple time statistics.

import time
import json

sessions = [] # All sessions are stored here. Old sessions are also loaded here through JSON.
current_session = {} # Acts as memory for the system, opens the current session and stores it.

def start_session():
    if "start_time" in current_session: # Stops user from starting session when a session is already present.
        print("Session already running. If you would like to end the session press '2'.")
    else:
        subject = input("Enter subject: ")
        current_session["subject"] = subject
        current_session["start_time"] = time.time()
        print("Session Started...")

def end_session():
    if "start_time" not in current_session: # Stops user from ending a non-existent session.
        print("Session not started. Please start a session first before trying to end one.")
    else:
        end_time = time.time()
        duration = float((end_time - current_session["start_time"]))

        subject = current_session["subject"] # Current subject.
        session_data = { # A dictionary of both the subject and the duration of the current session.
            "session": subject, 
            "duration": duration
        }

        try:
            with open("session_data.json", "r") as file:
                sessions = json.load(file) # Loads the json file to the sessions list.
        except: # I would use proper error handling here but I am keeping this system basic for now.
            sessions = []

        sessions.append(session_data)

        formatted = time.strftime("%H:%M:%S", time.gmtime(duration)) # Formats the duration into something user-friendly.

        print(f"Session ended. Duration: {formatted}")

        with open("session_data.json", "w") as file:
            json.dump(sessions, file, indent=4)
            file.close()
        current_session.clear() # Clears the current session so it is ready for the next session. Prevents errors.

def view_stats():
    with open("session_data.json", "r") as file:
        sessions = json.load(file) # Loads the sessions for the JSON file.
        
        total_duration = 0
        for session in sessions:
            total_duration += session["duration"] # Adds each session duration to the total.
        formatted = time.strftime("%H:%M:%S", time.gmtime(total_duration))

        print(f"Total today: {formatted}")

        for session in sessions:
            print(f"{session['session']}: {time.strftime('%H:%M:%S', time.gmtime(session['duration']))}") # Outputs it in a meaningful way.

def main():
    valid_inputs = ["1", "2", "3", "4"] # Valid user inputs.

    while True:
        print("1. Start session\n2. End session\n3. View stats\n4. Quit")
        usr_input = input(": ")

        if usr_input.isalpha():
            print("Please input a valid option.")
            continue
        if not usr_input in valid_inputs:
            print("Please input a valid option.")
            continue
        if usr_input.strip() == "1":
            start_session()
        if usr_input.strip() == "2":
            end_session()
        if usr_input.strip() == "3":
            view_stats()
        if usr_input.strip() == "4":
            return

if __name__ == "__main__":
    main()