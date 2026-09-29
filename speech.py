import pyttsx3
import speech_recognition as sr


# ---------------- TEXT TO SPEECH ----------------

try:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    if voices:
        engine.setProperty("voice", voices[0].id)

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

except Exception as e:
    print("TTS Error:", e)
    engine = None


def speak(text):
    print("Spidy:", text)

    if engine is not None:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("Speech Error:", e)


# ---------------- SPEECH RECOGNITION ----------------

listener = sr.Recognizer()
listener.energy_threshold = 300
listener.dynamic_energy_threshold = True
listener.pause_threshold = 0.8


def take_command():
    try:
        with sr.Microphone() as source:
            print("\nListening...")

            listener.adjust_for_ambient_noise(source, duration=1)

            audio = listener.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")
        command = listener.recognize_google(audio)
        command = command.lower().strip()

        print("You:", command)
        return command

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Could not understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        speak("Sorry, speech recognition service is unavailable.")
        return ""

    except Exception as e:
        print("Microphone Error:", e)
        return ""
