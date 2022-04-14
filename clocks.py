import time
import datetime
from threading import Thread
curr = 0
t = 0


def setCurrent():
  now = datetime.datetime.now()
  midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
  seconds = (now - midnight).seconds
  global curr
  curr = 86400 - seconds


def current_time():
  setCurrent()
  global curr
  print("Current time: \n")
  while curr:
      curr_hours = curr//3600
      curr_mins = curr//60 - (curr_hours*60)
      curr_secs = curr%60
      curr_timer = '{:02d}:{:02d}:{:02d}'.format(curr_hours,curr_mins,curr_secs)
      print(curr_timer, end="\r")
      time.sleep(1)
      curr-=1
  print("End of Day")
# get current time
def startTime(t):
  print("Pomodoro time: \n")
  while t:
      mins = t // 60
      secs= t % 60
      timer = '{:02d}:{:02d}'.format(mins,secs)
      print(timer, end="\r")
      time.sleep(1)
      t -=1
  print("End of time")
def main():
   selection = input("Enter 1 for clock or 2 for pomodoro clock:\n")
   if(selection == "1"):
       current_time()
   elif(selection == "2"):
       startTime(1500)
       startTime(300)
   cont = input("Another round?(Y/y): ")
   if(cont != 'Y' and cont != 'y'):
       exit()
   else:
       main()
main()
