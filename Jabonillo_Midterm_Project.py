# A simplified Python program that categorizes a person based on their phone number length.

def main():

    print("Welcome to the Phone Number Categorization Program!")

    while True:
        phone_number = input("Enter your phone number[Your starting number should be 0!]: ")
        cleaned_phone_number = ''.join(char for char in phone_number if char.isdigit())

        if cleaned_phone_number.startswith('0') and len(cleaned_phone_number) == 11:
            print("Your phone number is valid and categorized as a standard 11-digit number.")
            break
        else:
            print("OOPS! You might have inputted a incorrect number length or have put a different starting number other than 0! Sorry!.")

if __name__ == "__main__":
    main()