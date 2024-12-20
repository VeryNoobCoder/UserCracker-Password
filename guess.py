import itertools
import random
import string

username = ''.join(random.choices(string.ascii_lowercase, k=5))
print(f"Target username: {username}")
password = ''.join(random.choices(string.ascii_lowercase, k=4))
print(f"Target password: {password}")

print("Guessing username...")
for guess_tuple in itertools.product(string.ascii_lowercase, repeat=len(username)):
    guess = ''.join(guess_tuple)
    print(f"Guessing username: {guess}")
    if guess == username:
        print(f"Username cracked: {username}")
        break

print("Guessing password...")
for guess_tuple in itertools.product(string.ascii_lowercase, repeat=len(password)):
    guess = ''.join(guess_tuple)
    print(f"Guessing password: {guess}")
    if guess == password:
        print(f"Username cracked: {username}")
        print(f"Password cracked: {password}")
        break

