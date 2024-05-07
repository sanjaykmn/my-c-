print("welcome")
height = int(input("what is your height? "))
if height >= 120:
  print("you can ride")
  age = int(input("what is your age? "))
  if age < 12:
    print("you have to pay $5")
  elif age <= 18:
    print("you have to pay $7")
  else:
    print("you have to pay $12")
