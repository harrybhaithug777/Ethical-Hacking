import hashlib
import itertools
import string
import time

print("|||||        |||||           |||||||||||||||          ||||||||||||||||")
print("|||||        |||||          ||||||||||||||||          |||||||||||||||||")
print("|||||        |||||         |||||        |||||         ||||||||||||||||||")
print("|||||        |||||        |||||          |||||        |||||        |||||")
print("|||||--------|||||       |||||            |||||       |||||        |||||")
print("|||||--------|||||      ||||||||||||||||||||||||      |||||||||||||||||")
print("|||||--------|||||     ||||||||||||||||||||||||||     ||||||||||||||||")
print("|||||        |||||    |||||                  |||||    ||||||||")
print("|||||        |||||   |||||                    |||||   ||||| ||||")
print("|||||        |||||  |||||                      |||||  |||||  |||||")
print("|||||        ||||| |||||                        ||||| |||||   |||||")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")
print("     ")

target_pwd = str(input("Enter the password: \n"))

# Function to generate SHA-1 hash of a given password
def sha1_hash(password):
    return hashlib.sha1(password.encode()).hexdigest()

# Function to attempt to guess the password
def brute_force_sha1_cracker(target_hash, max_length=4):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    start_time = time.time()
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if sha1_hash(guess) == target_hash:
                end_time = time.time()
                print(f"Password cracked in {attempts} attempts and {end_time - start_time:.2f} seconds!")
                return guess

    print("Failed to crack the password.")
    return None

# Define the target password (for demonstration purposes)
target_password = target_pwd
target_hash = sha1_hash(target_password)

# Print the target hash (for verification)
print(f"Target SHA-1 hash: {target_hash}")

# Run the brute force SHA-1 password cracker
cracked_password = brute_force_sha1_cracker(target_hash)

if cracked_password:
    print(f"The cracked password is: {cracked_password}")
else:
    print("Password could not be cracked.")
