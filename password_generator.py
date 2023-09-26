import string, random

# Constants for password strength requirements

LETTERS_PERCENT = 30
# => 30% uppercase letters
# => 30% lowercase letters

NON_LETTERS_PERCENT = 20
# => 20% digits
# => 20% punctuations and special characters


def get_valid_password_length() -> int:

    while True:
        # Ensure that the user will enter valid integers
        print('Please enter password length:')
        password_length = input('')

        try:
            password_length = int(password_length)
            if password_length < 6:
                print('Password length must be at least 6 characters')
            else:
                break
        except ValueError:
            print('Please enter numbers only, try again!')
    return password_length

def generate_password(password_length: int) -> str:

    """
    Description: The method will generate strong password
    Args: integer
        password length
    Returns: string
        the output password
    """

    # Prepare all characters, digits, and punctuations as lists
    lowercase_letters   = list(string.ascii_lowercase)
    uppercase_letters   = list(string.ascii_uppercase)
    digits              = list(string.digits)
    punctuations        = list(string.punctuation)
    password            = []

    # Randomize all characters and digits in-place
    random.shuffle(lowercase_letters)
    random.shuffle(uppercase_letters)
    random.shuffle(digits)
    random.shuffle(punctuations)

    password_part_one = round(password_length * (LETTERS_PERCENT/100))
    password_part_two = round(password_length * (NON_LETTERS_PERCENT/100))

    # Append lower & upper case characters to the password
    for i in range(password_part_one):
        password.append(lowercase_letters[i])
        password.append(uppercase_letters[i])

    # Append digits and punctuations to the password
    for i in range(password_part_two):
        password.append(digits[i])
        password.append(punctuations[i])


    #############################################################################
    # Some bugs may appear when we divide the password parts due to round method
    # and will also appear if you use any other method for rounding,
    # e.g. if the user input is 15, the returned password will be 14 characters,
    # I think this problem will sometimes cause one character (+/-)
    # in the password with different input length, so we will check the ouput
    # password length before printing it to the user :)
    #############################################################################

    if password_length == len(password):
        pass
    elif password_length - len(password) == 1:
        password.append(random.choice(punctuations))
    elif len(password) - password_length == 1:
        password.pop()


    # Shuffle password again due to more security
    random.shuffle(password)
    password = ''.join(password)
    return password

if __name__ == '__main__':
    password_length = get_valid_password_length()
    password = generate_password(password_length)
    print(f"Your Generated Password is: {password}")
