
# Importing the pyttsx3 text-to-speech library
import pyttsx3 as p

# Initializing the engine
engine = p.init()

# Adding a phrase to be spoken
engine.say("make america great again")

# Running the speech engine to speak the queued phrase
engine.runAndWait()
