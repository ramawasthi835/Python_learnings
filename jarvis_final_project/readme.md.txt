
# 🧠 Jarvis - A Python Voice Assistant

Jarvis is a simple voice-activated assistant built with Python. It listens for the wake word "Jarvis" and responds to a range of commands — from opening websites and playing music to fetching the latest news using NewsAPI.

---

## 🚀 Features

- 🎙️ **Voice Recognition** using `speech_recognition`
- 🗣️ **Text-to-Speech** using `pyttsx3`
- 🌐 **Web Automation** to open popular websites
- 🎵 **Play Music** from a custom music library
- 📰 **Read News** headlines using [NewsAPI.org](https://newsapi.org)
- 💤 **Sleep Command** to exit

---

## 📂 Project Structure

```
Jarvis/
├── jarvis.py              # Main Python file
├── musiclib.py            # Custom music library (dictionary of song names & URLs)
├── README.md              # Project documentation
```

---

## 🛠️ Requirements

Install the required Python packages using pip:

```bash
pip install speechrecognition pyttsx3 requests
```

> ⚠️ For `speechrecognition`, you may also need to install PyAudio:
```bash
pip install pipwin
pipwin install pyaudio
```

---

## 🔑 Setup Your NewsAPI Key

1. Create a free account at [newsapi.org](https://newsapi.org).
2. Replace the `newsapi` key in the script with your own API key:
   ```python
   newsapi = "YOUR_API_KEY_HERE"
   ```

---

## 🧠 How It Works

1. The program listens for the wake word **"Jarvis"**.
2. Once activated, it asks for a command (e.g., "Open Google", "Play Alan", "News").
3. The assistant processes and executes the command using predefined actions.

### 🗒️ Sample Commands:

- `Jarvis` → Wake the assistant
- `Open YouTube` → Opens YouTube in your default browser
- `Play [song name]` → Plays song from custom musiclib
- `News` → Reads out top 5 headlines
- `Sleep` → Terminates the assistant

---

## 🧪 Demo

> 🔗 *[Insert video link or upload demo.mp4 here]*  
*(E.g., a short screen recording using OBS, Loom, or Windows screen recorder)*

---

## 📌 Notes

- For accurate voice recognition, ensure you’re in a quiet environment.
- `musiclib.py` should contain a dictionary with song names and URLs (YouTube/Spotify etc.).
- You can extend this project by adding:
  - File system automation
  - Alarms or reminders
  - Email or message reading

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add more voice commands, improve error handling, or refactor code, feel free to open a pull request.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [NewsAPI](https://newsapi.org)