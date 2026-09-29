import os
import subprocess
from pathlib import Path
from speech import speak


def handle_system_command(command):
    # Shutdown
    if "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
        return True

    # Restart
    if "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")
        return True

    # Lock
    if "lock" in command:
        speak("Locking the system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return True

    # Log off
    if "log off" in command:
        speak("Logging off the system.")
        os.system("shutdown /l")
        return True

    # Windows settings
    if "check my laptop updates" in command:
        speak("Opening Windows Update settings.")
        os.system("start ms-settings:windowsupdate")
        return True

    if "open settings" in command:
        speak("Opening Windows Settings.")
        os.system("start ms-settings:")
        return True

    # Battery report
    if "check my laptop battery" in command:
        speak("Generating your battery report.")

        try:
            report_path = Path.home() / "battery-report.html"

            subprocess.run(
                [
                    "powercfg",
                    "/batteryreport",
                    "/output",
                    str(report_path),
                ],
                check=False,
            )

            if report_path.exists():
                speak("Battery report generated.")
                os.startfile(report_path)
            else:
                speak("Sorry, I could not generate the battery report.")

        except Exception as e:
            print("Battery report error:", e)
            speak("Sorry, I could not generate the battery report.")

        return True

    # Camera
    if "open camera" in command:
        speak("Opening Camera.")
        os.system("start microsoft.windows.camera:")
        return True

    # Sleep
    if "turn on sleep mode" in command:
        speak("Putting the computer to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return True

    return False
