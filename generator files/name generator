import random

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

length = random.randint(3,9)

def generate_pronounceable_name(length=length):
    name = []
    for i in range(length):
        if i % 2 == 0:
            name.append(random.choice(consonants))
        else:
            name.append(random.choice(vowels))
    return ''.join(name)

print(generate_pronounceable_name())
