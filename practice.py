def sumNested(arr):
    result = 0
    for i in range(0, len(arr)):
        if type(arr[i]) is not int:
            result +=sumNested(arr[i])
        else:
            result += arr[i]

    return result


def radius_sort(arr):
    result = []
    for i in arr:

        area = 3.142 * i**2
        result.append(area)

    return result

def main():
    radius = input("Enter 10 radius separated by spaces").split()
    radius = [int(radii) for radii in radius]

    sorted_area = radius_sort(radius)

    print(sorted_area)




import calendar


