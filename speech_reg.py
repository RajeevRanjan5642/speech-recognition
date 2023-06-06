

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
except OSError :
    print("Flac conversion utility not available")
    
 # NOTE: Might get an error something like this that i got:
 #    OSError: FLAC conversion utility not available - consider installing the FLAC command 
 #    line application by running `apt-get install flac` or your operating system's equivalent
 #   Flac:A FLAC encoder is required to encode (convert into coded form) the audio data to send to the API.
 #   Don't worry just follow the following steps:
 #   1.Download flac (https://sourceforge.net/projects/flac/) in your PC.
 #   2.You will get a zip-file. Extract it. 
 #   3.Inside the folder you will see win32 and win64 subfolders.
 #   4.If your system is 32-bit open win32 folder or if it is 64-bit open win64.
 #   5.Inside these subfolders you will find executable file(flac.exe)
 #   6.Move the executable file(flac.exe) into your System32 directory(C:\Windows\System32) 
 #     and rename it as flac(remove.exe).
     
    
    

