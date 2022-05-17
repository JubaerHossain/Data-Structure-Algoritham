#Selection Sort

def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if(arr[j]< arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == '__main__':
    arr = [5,2,4,6,1,3]
    print(selectionSort(arr))


    #time complexity: O(n^2) because of nested loops and swaps in the inner loop 
    #space complexity: O(1) because no extra space is used 




