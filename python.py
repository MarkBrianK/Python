def fizzBuzz(n):
    result = []

    for i in range(1, n + 1):
        add = ""

        if i % 3 == 0:
            add += "Fizz"

        if i % 5 == 0:
            add += "Buzz"

        if add == "":
            result.append(i)
        else:
            result.append(add)
    return result


def twoSum(arr, S):
    hashTable = {}

    for i in range(0, len(arr)):
        sumMinusElement = S - arr[i]

    if sumMinusElement in hashTable:
        return True
    hashTable[arr[i]] = True

    return False


def sumNested(arr):
    result = 0
    for i in range(0, len(arr)):
        if type(arr[i]) is not int:
            result += sumNested(arr[i])
        else:
            result += arr[i]
    return result


def clockAngle(hour, mins):
    h = 0.5 * (60 * hour + mins)
    m = 6 * mins
    angle = abs(h - m)
    if angle > 180:
        return 360 - angle
    else:
        return angle


import math


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            return False
    return True


def count_occurrences():
    # Initialize a dictionary to store occurrences of numbers
    occurrences = {}

    # Input integers from the user
    nums = input("Enter integers between 1 and 100 separated by spaces: ").split()

    # Count occurrences of each number
    for num in nums:
        num = int(num)
        if 1 <= num <= 100:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1

    # Print the occurrences
    for num, count in occurrences.items():
        if count == 1:
            print(f"{num} occurs 1 time")
        else:
            print(f"{num} occurs {count} times")


# Call the function to execute the program
#

import random


def shuffle(lst):
    # Iterate over the list in reverse order
    for i in range(len(lst) - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        # Swap the elements at indices i and j
        lst[i], lst[j] = lst[j], lst[i]
    return lst


def main():
    # Prompt the user to enter five numbers
    numbers = input("Enter five numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    # Shuffle the numbers
    shuffled_numbers = shuffle(numbers)

    # Display the shuffled numbers
    print("Shuffled numbers:", shuffled_numbers)


# if __name__ == "__main__":
#     main()


def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the last element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main():
    # Prompt the user to enter ten numbers
    numbers = input("Enter ten numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    # Apply selection sort to the numbers
    sorted_numbers = selection_sort(numbers)

    # Display the sorted numbers
    print("Sorted numbers:", sorted_numbers)


# if __name__ == "__main__":
#     main()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Test program
if __name__ == "__main__":
    numbers = []
    for i in range(10):
        numbers.append(int(input("Enter a number: ")))
    bubble_sort(numbers)
    print("Sorted numbers:", numbers)


def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == "Q":
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    return True


def solve_queens(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = "Q"
            if solve_queens(board, col + 1):
                return True
            board[i][col] = " "
    return False


if __name__ == "__main__":
    board = [[" " for _ in range(8)] for _ in range(8)]
    if solve_queens(board, 0):
        print_board(board)
    else:
        print("No solution exists.")
import random


def simulate_bean_machine(balls, slots):
    paths = []
    for _ in range(balls):
        path = "".join(random.choice("LR") for _ in range(slots - 1))
        paths.append(path)
        print(path)
    histogram = [0] * slots
    for path in paths:
        position = path.count("R")
        histogram[position] += 1
    print("\n".join("O" * count for count in histogram))


if __name__ == "__main__":
    balls = int(input("Enter the number of balls to drop: "))
    slots = int(input("Enter the number of slots in the bean machine: "))
    simulate_bean_machine(balls, slots)
import random


def simulate_bean_machine(balls, slots):
    paths = []
    for _ in range(balls):
        path = "".join(random.choice("LR") for _ in range(slots - 1))
        paths.append(path)
        print(path)
    histogram = [0] * slots
    for path in paths:
        position = path.count("R")
        histogram[position] += 1
    print("\n".join("O" * count for count in histogram))


if __name__ == "__main__":
    balls = int(input("Enter the number of balls to drop: "))
    slots = int(input("Enter the number of slots in the bean machine: "))
    simulate_bean_machine(balls, slots)


def locker_puzzle(n):
    lockers = [False] * n
    for i in range(1, n + 1):
        for j in range(i - 1, n, i):
            lockers[j] = not lockers[j]
    return [i + 1 for i in range(n) if lockers[i]]


if __name__ == "__main__":
    open_lockers = locker_puzzle(100)
    print("Open lockers:", open_lockers)

import random


def select_word(words):
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


if __name__ == "__main__":
    words = ["write", "that", "program"]  # You can add more words
    play_again = "y"
    while play_again.lower() == "y":
        word_to_guess = select_word(words)
        guessed_letters = []
        misses = 0
        print(
            "(Guess) Enter a letter in word",
            display_word(word_to_guess, guessed_letters),
        )
        while "*" in display_word(word_to_guess, guessed_letters):
            guess = input("> ")
            if guess in guessed_letters:
                print(guess, "is already in the word")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print(display_word(word_to_guess, guessed_letters))
            else:
                misses += 1
                print(guess, "is not in the word")
            print(
                "(Guess) Enter a letter in word",
                display_word(word_to_guess, guessed_letters),
            )
        print("The word is", word_to_guess + ". You missed", misses, "time")
        play_again = input("Do you want to guess another word? Enter y or n> ")
import random


def simulate_coupon_collecting():
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    cards_collected = set()
    picks = 0
    while len(cards_collected) < len(suits):
        pick = (random.randint(1, 13), random.choice(suits))
        if pick not in cards_collected:
            picks += 1
            cards_collected.add(pick)
            print(f"{pick[0]} of {pick[1]}")
    print("Number of picks:", picks)


if __name__ == "__main__":
    simulate_coupon_collecting()


# Return true if the card number is valid
def isValid(number):
    return (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0


# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    total = 0
    num_str = str(number)
    for i in range(len(num_str) - 2, -1, -2):
        digit = int(num_str[i]) * 2
        total += getDigit(digit)
    return total


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    if number < 10:
        return number
    else:
        return (number // 10) + (number % 10)


# Return sum of odd place digits in number
def sumOfOddPlace(number):
    total = 0
    num_str = str(number)
    for i in range(len(num_str) - 1, -1, -2):
        total += int(num_str[i])
    return total


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    return getPrefix(number, getSize(d)) == d


# Return the number of digits in d
def getSize(d):
    return len(str(d))


# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
    return int(str(number)[:k])


if __name__ == "__main__":
    card_number = int(input("Enter a credit card number: "))
    if isValid(card_number):
        print("Valid credit card number")
    else:
        print("Invalid credit card number")
