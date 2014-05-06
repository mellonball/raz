import re
import rasp

WORDS = ["LITE", "ON", "OFF"]
#veraIP = rasp.getIP()  don't need this anymore when integrating with the hub. will talk to the hub instead.

def handle(text, mic, profile):
   """
      Responds to user input by printing out the command.
      Eventually it will send the command to the hub, which will execute it.
   """
   #heard lite
   #print text
   mic.say("You said " + text)
   #rasp.toggleLamp(veraIP, text.lower())       will need to send a request to the hub voice recognition app which will toggle the switch as requested for us through vera driver


def isValid(text):
   print text
   return bool(re.search(r'\blite\b', text, re.IGNORECASE))
