#quick sort

from dataclasses import dataclass


def quickSort(data):
    first = 0
    last = len(data) -1

    quickSortHelper(data,first,last)


def quickSortHelper(data,first,last):
    # print (data,first,last)
    if first < last:

        dividedPoint = partition(data,first,last)
        # print(data,first,dividedPoint-1)
        quickSortHelper(data,first,dividedPoint-1)
        quickSortHelper(data,dividedPoint+1,last)


def partition(data,first,last):
    pivotvalue = data[first]
    # print("pivotvalue",pivotvalue)
    leftmark = first+1
    rightmark = last

    # print("leftmark",leftmark)
    # print("rightmark",rightmark)
    done = False
    while not done:

        while leftmark <= rightmark and data[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            # print('lol',leftmark)

        while data[rightmark] >= pivotvalue and rightmark >= leftmark:
            # print('lol2',rightmark)
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp
            # print('else',data)

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp
    # print('temp',data)


    return rightmark

data = [29,10,14,37,15]
quickSort(data)
print(data)