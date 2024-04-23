import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import smtplib
import os

def speak(text) :
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty("voices")
    engine.setProperty("voice" , voice[0].id)
    engine.setProperty("rate" , 200) 
    print(f"jarvis : {text}")
    engine.say(Text=text)
    engine.runAndWait

def listen(): 
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source :
        print("  ")
        print("listening.....")
        r.pause_threshold = 0.5
        audio = r.listen(source , phrase_time_limit=3)

        try :
             print("  ")
             print("REcognizing.....")
             query = r.recognize_google(audio , language = "en-in")
             print(f"jarvis : {query}")

        except Exception as e : 
            print(e)
            return ""
        return query
  
 
listen()

 

if 1 :
     query = listen().lower()

     if "wikipedia" in query :
         speak("searching wikipedia....")
         query = query.replace("wikipedia" , "")
         results = wikipedia.summary(query , sentences = 2 )
         speak("according to wikipedia....")
         print(results)
         speak(results)
        
     elif "open youtube" in query :
         webbrowser.open("youtube.com")

     elif "open google" in query :
         webbrowser.open("google.com")
         
     elif "open stackoverflow" in query :
         webbrowser.open("stackoverflow.com")   

     elif "open youtube" in query :
         webbrowser.open("youtube.com")

     elif "the time" in query :
         strTime = datetime.now().strftime("%H:%M:%S")
         speak(f"sir , the time is {strTime}")

     
#speak(f"Playing {search_query} on YouTube.")
         
     #elif "email to omkar" in query : 
      #  try : 
      #       speak("what should i say ")
      ##       content = listen()
        #     to = "youeEmail@gmail.com"
         #    sendEmail(to , content) 
          #   speak("email has been send")

        #except Exception as e :
         #   print(e)
          #  speak("sorry , my friend I am nt able to send this email")


