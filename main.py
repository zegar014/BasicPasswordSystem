import hashlib
import os
import random
import string

saltchars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]}|;:,.<>?\/~`"
saltlength = random.randint(12, 128)
salt = ''.join(random.choice(saltchars) for _ in range(saltlength)) # Randomizing salt

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1. Register')
        print('2. Login')
        print('')
        menu = input('> ').strip().lower()
        if menu in ('1', '1.', 'reg', 'register'):
            input('Enter your username: ')
            password = input('Enter your password: ')
            saltypass = password + salt
            hash_pass = hashlib.sha256(saltypass.encode("utf-8")).hexdigest() # Combining your password with salt and hashing it
        elif menu in ('2', '2.', 'log', 'login'):
            typed_password = input('Enter your password: ')
            saltytype = typed_password + salt
            hash_type = hashlib.sha256(saltytype.encode("utf-8")).hexdigest() # Combining entered password with salt and hashing it
            if hash_type == hash_pass:
                input('Logged in. ')
            else:
                input('Declined. ')
                break

if __name__ == '__main__': 
    main()