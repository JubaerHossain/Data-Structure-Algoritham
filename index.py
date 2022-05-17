#bubble sort

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


if __name__ == '__main__':

    data = [3, 5, 1, 4, 2]
    print(bubble_sort(data))
    

