 
from random import choice, randint

class River:
  def __init__(self, size, num_bears, num_fish):
    self.map = [["🟦 "] * size for i in range(0, size)]
    self.size = size
    self.num_bears = num_bears
    self.num_fish = num_fish
    self.animals = []
    self.babies = []
    self.population = len(self.animals)
    self.__initial_population()
  
  def __initial_population(self):
    for i in range(self.num_bears):
      self.place_baby(Bear)
    for i in range(self.num_fish):
      self.place_baby(Fish)
        
  def place_baby(self, creature):
    y = randint(0, len(self.map)-1)
    x = randint(0, len(self.map[y])-1)
    spot = self.map[y][x]
    while spot != "🟦 ":
      y = randint(0, len(self.map)-1)
      x = randint(0, len(self.map[y])-1)
      spot = self.map[y][x]
    #print(spot, type(spot), "!!")
    if creature == Bear:
      anim = Bear(x, y)
    else:
      anim = Fish(x, y)
    self.map[y][x] = anim
    self.animals.append(anim)

  def animal_death(self, creature):
    #print(creature)
    #print(self.animals)
    self.animals.remove(creature)
    self.map[creature.y][creature.x] = "🟦 "

  def redraw_cells(self,creature):
    riv[creature.y][creature.x] = "🟦 "
    riv[spotY][spotX] = creature

  def new_day(self):
    for anim in self.animals:
      anim.move(anim, self, self.babies)
    for baby in self.babies:
      self.place_baby(baby)

    self.babies.clear()
    for anim in self.animals:
      anim.bred_today = False
    for anim in self.animals:
      if anim == Bear:
        anim.starve(self)
    
    check = []
    for i in self.map:
      check.append(i)
    if "🟦 " not in check:
      return False
    else:
      pass
    
#ETC----------
  def __getitem__(self,k):
    return self.map[k]

  def __str__(self):
    map_formatted = ""
    for r in range(self.size):
      for i in self.map[r]:
        map_formatted += str(i)
      map_formatted += "\n"
    return map_formatted

#ANIMALS-----------
class Animal:
  def __init__(self, x, y):
    self.y = y
    self.x = x
    self.bred_today = False
  
  def death(self, riv):
    print(f"!{self} died!")
    riv.animal_death(self)

  def move(self, creature, riv, babies):
    print(creature.y)
    # randint -1 - 1 for y & x -- if y or x > len(self.map), reroll value
    spotY = self.y + randint(-1, 1)
    spotX = self.x + randint(-1, 1)
    while spotY >= riv.size:
      try:
        spotY = self.y + randint(-1, 1)
      except:
        print("invalid")
    while spotX >= riv.size:
      try:
        spotX = self.x + randint(-1, 1)
      except:
        print("invalid")
    #print(spotY, spotX)
    spot = riv[spotY][spotX]
    self.collision(riv, creature, babies, spot)
    riv[creature.y][creature.x] = "🟦 "
    riv[spotY][spotX] = creature
    #riv.redraw_cells(riv, creature)



  def collision(self, map, creature, babies, spot):
    print(f"!{spot} collided with {creature}!")
    if type(spot) == type(creature):
      print(f"!{creature},{spot} bred!")
      babies.append(creature)
      creature.bred_today = True
    else:
      if type(creature) == Bear and spot != "🟦 ":
        creature.consume(spot, map)
      elif type(spot) == Bear and creature != "🟦 ":
        spot.consume(creature, map)
    #if tile == tile, breed - else, Bear.consume


class Fish(Animal):
  def __init__(self, x, y):
    super().__init__(x, y)
  def __str__(self):
    return "🐟 "

class Bear(Animal):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.max_lives = 3
    self.lives = 3
    self.eaten_today = False

  def starve(self, riv):
    if self.eaten_today == False:
      self.lives -= 1
      if self.lives == 0:
        self.death(riv)
    self.eaten_today = False

  def consume(self, creature, riv):
    #print("!Fish Consumed!")
    self.eaten_today = True
    self.lives += 1
    creature.death(riv)
  
  def __str__(self):
    return "🐻 "