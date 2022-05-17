#linear search

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_linear(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


print(find_linear(data, 5))