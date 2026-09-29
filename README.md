# 🕷️ Spidy - Desktop Voice Assistant

Spidy is a Python-based desktop voice assistant for Windows.

It can listen to voice commands, speak responses, open websites and Windows applications, control basic Windows functions, play YouTube content, search Wikipedia, tell jokes, and provide the current date and time.

## ✨ Features

- 🎤 Voice command recognition
- 🔊 Text-to-speech responses
- 🌐 Open websites
- ▶️ Play songs/videos on YouTube
- 📚 Wikipedia search
- 😂 Tell jokes
- 🕒 Current time and date
- 💻 Open Windows applications
- 🔒 Lock Windows
- 🔄 Restart Windows
- ⏻ Shutdown Windows
- 😴 Sleep mode
- 🔋 Generate Windows battery report
- ⚙️ Open Windows Settings and Windows Update

## 📁 Project Structure

```text
Spidy-Desktop-Voice-Assistant/
│
├── main.py
├── speech.py
├── browser_commands.py
├── system_commands.py
├── app_commands.py
├── info_commands.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Spidy-Desktop-Voice-Assistant.git
cd Spidy-Desktop-Voice-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows CMD:

```bash
venv\Scripts\activate
```

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Spidy

```bash
python main.py
```

## 🎤 Example Voice Commands

```text
open google
open youtube
open github
open chatgpt
open notepad
open calculator
open command prompt
open excel
open word

play shape of you

who is Elon Musk
what is Python

what is the time
what is the date
tell me a joke

check my laptop battery
check my laptop updates
open settings

lock
restart
shutdown
turn on sleep mode

hello
how are you
bye
```

## ⚠️ Windows Notes

This project uses Windows-specific commands for shutdown, restart, lock, sleep, Windows Settings, Camera, Excel, and Word.

A working microphone is required for voice recognition.

`SpeechRecognition` uses Google's speech recognition service through the library, so an internet connection may be required for recognition.

Microsoft Word and Excel must be installed if you want Spidy to open them using their Windows commands.

## 🔐 Safety

Some commands can immediately affect your computer:

- `shutdown`
- `restart`
- `lock`
- `log off`
- `turn on sleep mode`

Use these commands carefully.

## 🚀 Future Improvements

Possible future upgrades:

- Wake word: **"Hey Spider"**
- Spider-Man themed GUI
- OpenAI-powered conversational answers
- Weather information
- News search
- Email and WhatsApp automation
- Application launcher
- Custom voice
- Conversation history
- Better error handling
- Configuration file for customizable commands

## 👨‍💻 Author

Created as a Python desktop voice assistant project.

---

⭐ If you find this project useful, consider starring the repository on GitHub.
