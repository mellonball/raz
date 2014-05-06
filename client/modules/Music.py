import re
#import hubmusic

WORDS = ["MUSIC"]
#veraIP = rasp.getIP()

def handle(text, mic, profile):
   """
      Responds to user input by printing out the command.
      Eventually it will send the command to the hub, which will execute it.
   """
   #it heard the word Music
   mic.say("You said " + text)

   #contact the hub requesting a file (NAMED songoptions.txt that overwrites) containg 3 random songs and numbers on the same line
   #hubmusic.getoptions()

   #for line in file, read out the line which will be (1 jayz - brush your shoulders off ....) 
   with open("songoptions.txt", "r") as searchfile:
      for line in searchfile:
         mic.say(line.strip())

   #listen for user input
   #if user chooses a valid number, send that number to the HUB and the HUB will send over that song
   #play the song

   #probably import hubmusic and in there function playsong. 
   #rasp.toggleLamp(veraIP, text.lower())


def isValid(text):
   print text
   return bool(re.search(r'\bmusic\b', text, re.IGNORECASE))
