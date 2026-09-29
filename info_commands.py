import datetime
import pyjokes
import wikipedia
from speech import speak


def handle_info_command(command):
    # Date and time
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
        return True

    if "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)
        return True

    # Wikipedia - Who is
    if command.startswith("who is"):
        person = command.replace("who is", "", 1).strip()

        if person:
            try:
                speak("Searching Wikipedia.")
                info = wikipedia.summary(person, sentences=2)
                print("Wikipedia:", info)
                speak(info)

            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")

            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find that person.")

            except Exception as e:
                print("Wikipedia error:", e)
                speak("Sorry, I couldn't find information.")

        return True

    # Wikipedia - What is
    if command.startswith("what is"):
        thing = command.replace("what is", "", 1).strip()

        if thing:
            try:
                speak("Searching Wikipedia.")
                info = wikipedia.summary(thing, sentences=2)
                print("Wikipedia:", info)
                speak(info)

            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results. Please be more specific.")

            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find that information.")

            except Exception as e:
                print("Wikipedia error:", e)
                speak("Sorry, I couldn't find information.")

        return True

    # Joke
    if "joke" in command:
        try:
            joke = pyjokes.get_joke()
            print("Joke:", joke)
            speak(joke)
        except Exception:
            speak("Sorry, I couldn't find a joke.")
        return True

    # Greetings
    if "hello" in command or "hi" in command:
        speak("Hello! How are you?")
        return True

    if "how are you" in command:
        speak("I am fine. Thank you for asking.")
        return True

    return False
