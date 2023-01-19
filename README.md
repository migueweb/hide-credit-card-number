# Hide the credit card number

## The challenge
Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four.

## Solution
```python
def hideNumber(cardNumber):
    # Check lenght
    if len(cardNumber) < MIN_LEN or len(cardNumber) > MAX_LEN:
        print("Invalid Number")
    else:
        counter = 0
        for char in cardNumber:
            cardNumber = cardNumber.replace(char,"*", 1)
            counter += 1
            if counter == len(cardNumber) - LAST_NUMBERS:
                break
```
**>>> [Full solution](main.py) <<<**

## Author
Github - [@migueweb](https://github.com/migueweb)