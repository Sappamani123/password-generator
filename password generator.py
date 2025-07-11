import random
import string
def strong_password(length):
    if length < 6:
        return "Password length should be at least 6 for a strong password."

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    #print(password)
    password += [random.choice(all_chars) for _ in range(length-4)]
    random.shuffle(password)
    return ''.join(password)
length=int(input(" enter length you want for your password:"))   
print("Strong password:", strong_password(length))
