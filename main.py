from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    pause = int(input("Press 2 anytime to stop playback and go back to the menu: "))
    if pause == 2:
      source.pause = True
    # Start taking user input and doing something with it
      return
    else:
      continue
while True:
  os.system("clear")
  print("   MyPOD Music Player  ")
  time.sleep(3)
  print("Press 1 to Play")
  time.sleep(3)
  print("Press 2 to Exit")
  time.sleep(3)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue