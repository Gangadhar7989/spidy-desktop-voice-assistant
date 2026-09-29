import os
import pywhatkit
from speech import speak


def handle_app_command(command):
    # Windows applications
    if "open notepad" in command:
        speak("Opening Notepad.")
        os.system("start notepad")
        return True

    if "open calculator" in command:
        speak("Opening Calculator.")
        os.system("start calc")
        return True

    if "open command prompt" in command:
        speak("Opening Command Prompt.")
        os.system("start cmd")
        return True

    if "open excel" in command:
        speak("Opening Microsoft Excel.")
        os.system("start excel")
        return True

    if "open word" in command:
        speak("Opening Microsoft Word.")
        os.system("start winword")
        return True

    # YouTube
    if command.startswith("play"):
        song = command.replace("play", "", 1).strip()

        if song:
            speak("Playing " + song)

            try:
                pywhatkit.playonyt(song)
            except Exception as e:
                print("YouTube error:", e)
                speak("Sorry, I could not play that song.")
        else:
            speak("Please tell me the song name.")

        return True

    return False
