# ZASS Voice Assistant Prototype

A Python desktop voice-assistant prototype combining speech recognition, speech synthesis, an Eel web interface and command automation.

## Status and authentication

This is a Windows-oriented academic prototype. A legacy authentication-cookie file remains tracked in repository history and requires account-side session revocation and an explicitly reviewed removal. Do not reuse published cookies. The updated chatbot configuration reads a separate local cookie file through `ZASS_COOKIE_PATH` and refuses to use the known tracked legacy path.

## Problem and architecture

The prototype explores voice interaction with desktop and browser tasks. SpeechRecognition captures commands; pyttsx3 speaks responses; Eel connects Python handlers with HTML/CSS/JavaScript; SQLite stores commands and contacts. HugChat provides an external chatbot integration. Porcupine is used for wake-word detection.

| Path | Responsibility |
|---|---|
| `main.py` | Start the Eel interface and Microsoft Edge app window |
| `run.py` | Attempt concurrent assistant/wake-word processes |
| `moteur/commend.py` | Recognition, speech output and command dispatch |
| `moteur/features.py` | Application/browser commands and external integrations |
| `moteur/database.py` | SQLite access and commented initialization examples |
| `site/` | Frontend and vendor assets |

## Development setup

Use Windows, a microphone/audio output, Microsoft Edge and an isolated Python environment. Existing commands use `os.startfile` and Windows `start`; macOS/Linux compatibility is not established.

```powershell
git clone https://github.com/zik4O4/ZASS-PRG.git
cd ZASS-PRG
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install eel pyttsx3 SpeechRecognition pyaudio playsound pyautogui pywhatkit pvporcupine hugchat
```

This list reflects imports, not a tested lockfile. Audio drivers, service versions and Porcupine credentials need configuration. Modern Porcupine versions may require an access key that the existing wake-word code does not supply. Review the SQLite schema and local command mappings before launching; the committed database is a historical artifact rather than a verified clean seed database.

For the chatbot, obtain fresh cookies through your own supported account workflow and save them outside the repository or under the ignored `.local/` directory:

```powershell
$env:ZASS_COOKIE_PATH = "C:\path\outside\repository\cookies.json"
python main.py
```

Never commit this file. External recognition/chat services require network access and may change independently. Desktop messaging and calling handlers have real side effects; use your own test environment and explicit user actions.

## Existing interface asset

<img width="1217" height="683" alt="Existing ZASS interface screenshot" src="https://github.com/user-attachments/assets/6d4bf64c-4006-4253-be04-0d057b0152c2" />

## Known limitations

- `main.py` starts the assistant when imported, which complicates the multiprocessing path in `run.py`; that runner is not a verified startup procedure.
- Recognition error paths may leave a command undefined; broad exception handlers make debugging difficult.
- UI-driven messaging depends on window state and hard-coded navigation.
- Published cookies, personal sample contact information and database contents require cleanup before professional featuring.
- The prototype integrates services rather than demonstrating a locally trained speech or language model.

## Attribution and license

Original project assets and third-party vendor notices are preserved. No repository-level license has been selected.
