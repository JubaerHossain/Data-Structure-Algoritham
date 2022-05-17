#Binary Search

def find_binary(data, item):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = data[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

input = int(input("Enter a number to search for: "))

target = find_binary(data, input)

print("Searching for {} in {}".format(input, data))

print("Found {} at index {}".format(input, target))






