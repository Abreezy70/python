import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$'

length = input('password length')
length = int(length)

pcount = input('how many passwords do you need')
pcount = int(pcount)



for p in range(pcount):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)

