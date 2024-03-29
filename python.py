def fizzBuzz(n):
    result = []

    for i in range(1, n+1):
        add = ''

        if i % 3 == 0:
            add += "Fizz"

        if i % 5 == 0:
            add += 'Buzz'

        if add == '':
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
    if n<2:
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

if __name__ == "__main__":
    main()







