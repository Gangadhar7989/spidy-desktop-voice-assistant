from speech import speak, take_command
from browser_commands import handle_browser_command
from system_commands import handle_system_command
from app_commands import handle_app_command
from info_commands import handle_info_command


def main():
    speak("Hello, friend.")
    speak("I am Spidy.")
    speak("How can I help you?")

    while True:
        command = take_command()

        if not command:
            continue

        if command in {"exit", "stop", "bye"} or "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye, friend.")
            speak("Have a nice day.")
            break

        if handle_browser_command(command):
            continue

        if handle_system_command(command):
            continue

        if handle_app_command(command):
            continue

        if handle_info_command(command):
            continue

        speak("Sorry. I did not understand that command.")


if __name__ == "__main__":
    main()
