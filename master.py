import random
print("How many cats do you want?")
c = int(input())
o = 0
while o < c:
  x = random.randint(1, 3)
  if x == 1:
      print('Meow')
      o = o + 1
  elif x == 2:
      print('Purr')
      o = o + 1
  else:
      print('Ftt')
      o = o + 1
