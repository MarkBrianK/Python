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
