# Hide the credit card number

MIN_LEN = 16
MAX_LEN = 19
LAST_NUMBERS = 4

def hideNumber(cardNumber):
    # Check valid Lenght
    if len(cardNumber) < MIN_LEN or len(cardNumber) > MAX_LEN:
        print("Invalid Number")
    else:
        counter = 0
        for char in cardNumber:
            cardNumber = cardNumber.replace(char,"*", 1)
            counter += 1
            if counter == len(cardNumber) - LAST_NUMBERS:
                break
        print(f"Your card number is {cardNumber}")

input = input("Enter your card number: ")

hideNumber(input)