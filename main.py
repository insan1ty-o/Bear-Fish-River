# Matthew Fahnestock
# Bear Fish River
# Making a game of Bear Fish River
from ecosystem import *
import os
from time import sleep

SIMULATION_DAYS = 20
RIVER_SIZE = 10
START_BEARS = 10
START_FISH = 10

def main():
  r = River(RIVER_SIZE, START_BEARS, START_FISH)
  fullmap = False
  for day in range(SIMULATION_DAYS):
    while fullmap == False:
      print(f"{r}\n")
      sleep(1)
      #os.system("clear") 
      fullmap = r.new_day()

if __name__ == "__main__":
  main()