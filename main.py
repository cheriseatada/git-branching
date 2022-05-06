""" Git Branching """
from datetime import datetime

def good_morning():
  weekday = datetime.today().strftime("%A")
  print(f"Good morning! Happy {weekday}~")

good_morning()


