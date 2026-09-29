import webbrowser
from speech import speak


BROWSER_COMMANDS = {
    "open google": ("Google", "https://www.google.com"),
    "open youtube": ("YouTube", "https://www.youtube.com"),
    "open whatsapp": ("WhatsApp", "https://www.whatsapp.com"),
    "open facebook": ("Facebook", "https://www.facebook.com"),
    "open x": ("X", "https://x.com"),
    "open chatgpt": ("ChatGPT", "https://chatgpt.com"),
    "open instagram": ("Instagram", "https://www.instagram.com"),
    "open twitter": ("Twitter", "https://twitter.com"),
    "open linkedin": ("LinkedIn", "https://www.linkedin.com"),
    "open github": ("GitHub", "https://github.com"),
}


def handle_browser_command(command):
    for trigger, (name, url) in BROWSER_COMMANDS.items():
        if trigger in command:
            speak(f"Opening {name}")
            webbrowser.open(url)
            return True

    return False
