import string
import random

password = []

all_chars = list(
    string.ascii_letters +  # a-z + A-Z
    string.digits +         # 0-9
    string.punctuation      # Special characters like !@#...
)

for i in range(20):
    letter = random.choice(all_chars)
    password.append(letter)

print(''.join(password))
