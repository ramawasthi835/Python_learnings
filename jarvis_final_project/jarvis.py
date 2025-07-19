# Voice Assistant (Jarvis)
# Features: Speech recognition, command handling, opening websites, playing music, reading news via NewsAPI

import speech_recognition as sr       # For voice input
import webbrowser                     # To open websites
import pyttsx3                        # For text-to-speech
import musiclib                       # Custom music library (assumes dictionary of songs)
import requests                       # For API requests (NewsAPI)
import os                             # Optional: may be used for future expansions

# Initialize recognizer and TTS engine
recogniser = sr.Recognizer()
engine = pyttsx3.init()

# Your NewsAPI key, please get you own api from newsapi.
newsapi = "2c72a1af0fe94f049ec4d62dd3782fa4"

# Speak function using pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function to handle voice commands
def run_command(command):
    command = command.lower()  # Make command lowercase for consistent comparison

    if command == "sleep":
        exit()

    elif "open google" in command:
        webbrowser.open("www.google.com")

    elif "open facebook" in command:
        webbrowser.open("www.facebook.com")

    elif "open instagram" in command:
        webbrowser.open("www.instagram.com")

    elif "open youtube" in command:
        webbrowser.open("www.youtube.com")

    elif "open snapchat" in command:
        webbrowser.open("www.snapchat.com")

    elif "open gmail" in command:
        webbrowser.open("www.gmail.com")

    elif "open linkedin" in command:
        webbrowser.open("www.linkedin.com")

    # Play a song from the custom music library
    elif command.startswith("play"):
        song = command.split(" ")[1]  # Extract the song name (2nd word)
        music = musiclib.music[song]  # Get URL from your custom musiclib
        webbrowser.open(music)

    # Fetch top 5 news headlines using NewsAPI
    elif "news" in command:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data = response.json()

        if data["status"] == "ok":
            articles = data["articles"][:5]  # Get top 5 articles
            print("Number of articles:", len(articles))
            print("Top Headlines in India:\n")

            for i, article in enumerate(articles, 1):
                headline = article['title']
                print(f"{i}. {headline}")
                speak(f"Headline {i}: {headline}")
        else:
            print("Error:", data.get("message", "Something went wrong"))
            speak("Sorry, I couldn't fetch the news.")

    else:
        print("Command not recognized!!!")

# Start listening and responding
if __name__ == "__main__":
    speak("Initiating Jarvis...")

    while True:
        try:
            # Listen for the wake word "Jarvis"
            with sr.Microphone() as source:
                print("Listening...")
                audio = recogniser.listen(source, timeout=10, phrase_time_limit=1)

            print("Recognizing...")
            word = recogniser.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes Sir, How may I help you?")

                # Listen for actual command
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = recogniser.listen(source, timeout=4, phrase_time_limit=2)

                print("Recognizing...")
                command = recogniser.recognize_google(audio)
                print("Recognized command:", command)
                run_command(command)

        except Exception as e:
            print("Error:", e)

        