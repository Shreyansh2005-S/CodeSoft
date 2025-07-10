# Password Generator 
import random
import string

def generate_password(length):
    """Generates a random password of specified length."""
    if length < 4:
        return "Password length should be at least 4 characters for better password"
    
    #Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    #Ensure the password includes atleast one uppercase, one lowercase, number
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    #Fill the rest of the password length with random choices
    password += random.choices(characters, k=length - 4)

    #Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
