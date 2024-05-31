import random
import secrets

passcode=input(str("Enter passcode:"))
s=0

for character in passcode:
    s = s +ord(character)

secrets.SystemRandom(s)

print(int(random.random()*1000000000000))
    
input('')
