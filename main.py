import random


def lotteryResult(num1, num2, num3):

    """ This function will accept 3 distinct numbers from 1 to 15 and return a string "Hooray! you won!" if the user
    guesses one or two of the numbers, "It's a Jackpot!" if the user guessed all the numbers, and "Sorry, you were
    unlucky this time. Try again!" if the user didn't guess any of the numbers.  Each time the function is called it
    will generate 3 unique winning numbers from 1 to 15 and compare then to the ones the user passed as arguments in
    any order"""

    # Ensure the numbers are within the valid range
    if not all(1 <= n <= 15 for n in (num1, num2, num3)):
        return "Invalid input! Numbers must be between 1 and 15."

    # Generate 3 distinct winning numbers
    winning_numbers = set(random.sample(range(1, 16), 3))
    user_numbers = {num1, num2, num3}

    # Determine how many numbers match
    matches = len(user_numbers & winning_numbers)

    # Return the appropriate message
    print("The winning numbers are: ", winning_numbers)

    if matches == 3:
        return "It's a Jackpot!"
    elif matches > 0:
        return "Hooray! You won!"
    else:
        return "Sorry, you were unlucky this time. Try again!"


# Example usage
if __name__ == '__main__':
    print(lotteryResult(3, 7, 12))

