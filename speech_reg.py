

"""

Author   : Rajeev Ranjan
Date     : June 5 2023 8:01 PM
Objective: To create a speech to text converter using Google Speech Recognition API through python
 
"""

import speech_recognition as sr

#create a variable for storing/refering the sample audio file
audio_file=("sample.wav")

r=sr.Recognizer() #initialise the recogniser

with sr.AudioFile(audio_file) as source: #use audio_file as source
    audio=r.record(source) #extracts the audio file data
    
try:
    print(r.recognize_google(audio)) #recognize the audio using google speech recognition
    #exception handling
except sr.UnknownValueError :
    print("Google Speech Recognition could not understand audio")
except sr.RequestError :
    print("couldn't get the results from Google Speech Recognition")

